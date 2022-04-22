const path = require("path");
const { merge } = require("webpack-merge");
const common = require("./webpack.common.js");
const webpack = require("webpack");
const BundleTracker = require("webpack-bundle-tracker");
const VueLoaderPlugin = require("vue-loader/lib/plugin");

module.exports = merge(common, {
  mode: "development",
  devtool: "inline-cheap-source-map",
  output: {
    chunkFilename: "[name].chunk.js",
    publicPath: "http://127.0.0.1:8080/",
  },
  devServer: {
    // serve dev app.js from node server
    contentBase: path.join(__dirname, "./assets/bundles/"),
    host: "127.0.0.1",
    compress: true,
    port: 8080,
    inline: true,
    hot: true,
    headers: {
      "Access-Control-Allow-Origin": "*",
    },
  },
  plugins: [
    new BundleTracker({
      filename: "../mediusware_coding_test/static/vue/webpack-stats.json",
    }),
    new VueLoaderPlugin(),
    new webpack.DefinePlugin({
      "process.env": require("./conf/dev.env.js"),
    }),
  ],
});
