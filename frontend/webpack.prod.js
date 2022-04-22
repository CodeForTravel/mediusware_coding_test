const { merge } = require("webpack-merge");
const common = require("./webpack.common.js");
const webpack = require("webpack");
const BundleTracker = require("webpack-bundle-tracker");
const VueLoaderPlugin = require("vue-loader/lib/plugin");

module.exports = merge(common, {
  mode: "production",
  devtool: "source-map",
  bail: true,
  output: {
    filename: "[name].[chunkhash:8].js",
    chunkFilename: "[name].[chunkhash:8].chunk.js",
  },
  plugins: [
    new BundleTracker({
      filename: "../mediusware_coding_test/static/vue/webpack-stats.json",
    }),
    new VueLoaderPlugin(),
    new webpack.DefinePlugin({
      "process.env": require("./conf/prod.env.js"),
    }),
  ],
});
