const path = require('path'),
    ENVIRONMENTS = require('./frontend/env/env.types'),
    webpack = require('webpack'),
    autoprefixer = require('autoprefixer'),
    OptimizeCSSAssetsPlugin = require("optimize-css-assets-webpack-plugin"),
    UglifyJsPlugin = require('uglifyjs-webpack-plugin'),
    MiniCssExtractPlugin = require("mini-css-extract-plugin");

const rootDir = path.join(__dirname, '/frontend/'),
    distDir = path.resolve(__dirname, 'static/frontend');

const currentEnv = process.env.NODE_ENV,
    isDev = (devValue, prodValue) => {
        if (ENVIRONMENTS.DEVELOPMENT === currentEnv) {
            return devValue;
        }

        return prodValue;
    };

const config = {
     entry: {
         main: path.join(rootDir, 'pages/main/index.js'),
         contacts: path.join(rootDir, 'pages/contacts/index.js')
     },
     output: {
         path: distDir,
         filename: 'js/[name].bundle.js'
     },
     mode: currentEnv,
     plugins: [
        new MiniCssExtractPlugin({
          filename: 'css/[name].css',
          chunkFilename: 'css/[id].css'
        })
     ],
     watch: isDev(true, false),
     devtool: isDev('source-map', false),
     module: {
         rules: [
             {
                 test: /\.js$/,
                 loader: 'babel-loader',
                 exclude: /node_modules/,
                 query: {
                     presets: ['@babel/preset-env']
                 }
             },
             {
                    test: /\.(s)?css$/,
                    use: [
                        MiniCssExtractPlugin.loader,
                        {
                            loader: 'css-loader',
                            options: {
                                sourceMap: isDev(true, false)
                            }
                        },
                        {
                            loader: 'postcss-loader',
                            options: {
                                plugins: () => [autoprefixer({ browsers: ['last 2 version'] })]
                            }
                        },
                        {
                            loader: 'sass-loader',
                            options: {
                                includePaths: [
                                    path.join(__dirname, 'node_modules/normalize-scss/sass')
                                ]
                            }
                        }
                    ]
                },
         ]
     },
     stats: {
         colors: true
     }
 };

config.optimization = isDev({}, {
    minimizer: [
        new OptimizeCSSAssetsPlugin({
            cssProcessorPluginOptions: {
                preset: ['default', { discardComments: { removeAll: true } }],
            }
        }),
        new UglifyJsPlugin({
            uglifyOptions: {
                compress: {
                    inline: false
                },
                output: {
                    comments: false
                }
            }
        })
    ]
});

module.exports = config;