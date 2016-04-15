var path = require('path');
var webpack = require('webpack');

module.exports = {
    entry: './index.jsx',
    output: {
        path: __dirname, filename: 'build/app.js',
        sourceMapFilename: 'build/app.map'
    },
    devtool: '#source-map',
    module: {
        loaders: [
          {
              test: /.(jsx|js)?$/,
              loader: 'babel',
              exclude: /node_modules/,
              cacheDirectory: true,
              query: {
                  presets: ['es2015', 'react']
              }
          },
          {
              test: /.json?$/,
              loader: 'json-loader'
          }
        ]
    }
};
