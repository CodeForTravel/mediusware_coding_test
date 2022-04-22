const path = require("path");

module.exports = {
  context: __dirname,
  entry: { app: "./src/js/index" },
  output: {
    // serve production from static
    path: path.resolve("../mediusware_coding_test/static/vue"),
    filename: "app.js",
    publicPath: "/static/vue/",
  },
  optimization: {
    splitChunks: {
      chunks: "all",
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name(module) {
            // get the name. E.g. node_modules/packageName/not/this/part.js
            // or node_modules/packageName
            const packageName = module.context.match(
              /[\\/]node_modules[\\/](.*?)([\\/]|$)/
            )[1];

            // npm package names are URL-safe, but some servers don't like @ symbols
            return `yarn.${packageName.replace("@", "")}`;
          },
        },
      },
    },
  },
  node: {
    fs: "empty",
    net: "empty",
  },

  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: "babel-loader",
      },
      {
        test: /\.vue$/,
        loader: "vue-loader",
      },
      {
        test: /\.css$/i,
        use: ["style-loader", "css-loader"],
      },
      {
        test: /\.scss$/,
        use: ["style-loader", "css-loader", "sass-loader"],
      },
    ],
  },
  resolve: {
    alias: {
      vue: "vue/dist/vue.js",
    },
  },
};
