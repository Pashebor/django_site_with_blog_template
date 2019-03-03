const path = require('path'),
    webpack = require('webpack');

const rootDir = path.join(__dirname, '/frontend/'),
    distDir = path.resolve(__dirname, 'static/frontend');

 module.exports = {
     entry: {
         main: path.join(rootDir, 'pages/main/index.js'),
         contacts: path.join(rootDir, 'pages/contacts/index.js')
     },
     output: {
         path: path.resolve(distDir, 'js'),
         filename: '[name].bundle.js'
     },
     mode: 'development',
     module: {
         rules: [
             {
                 test: /\.js$/,
                 loader: 'babel-loader',
                 exclude: /node_modules/,
                 query: {
                     presets: ['@babel/preset-env']
                 }
             }
         ]
     },
     stats: {
         colors: true
     },
     devtool: 'source-map'
 };