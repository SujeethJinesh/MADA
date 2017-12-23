var webpack = require('webpack');  
module.exports = {  
  entry: [
    "./js/App.js"
  ],
  output: {
    path: __dirname + '/static',
    filename: "bundle.js"
  },
  module: {
    loaders: [
      {
        test: /\.js?$/,
        loader: 'babel-loader',
        query: {
          presets: ['es2015', 'react']
        },
        exclude: /node_modules/
      },
        {
            test: /\.css$/,
            exclude: /^node_modules$/,
            loader: 'style-loader!css-loader!autoprefixer-loader!sass-loader',
        },
        { test: /\.svg$/, loader: "file-loader" }
    ],
      resolve: {
        extensions: ['', '.js', '.jsx', '.css', '.svg'],
        modulesDirectories: [
          '/node_modules/'
        ]
    }
  },
  plugins: [
  ]
};
