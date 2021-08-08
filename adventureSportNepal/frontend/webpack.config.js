const path = require("path");
const webpack = require("webpack");
const ESLintPlugin = require('eslint-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    entry: "./src/index.tsx",
    output: {
        path: path.resolve(__dirname, "./static/frontend"),
        filename: "[name].js",
    },
    module: {
        rules: [

            {
                test: /\.(ts|tsx|js|jsx)$/,
                exclude: /node_modules/,
                use: [
                    {
                        loader: 'babel-loader?'
                    },
                ]
            },
            {
                test: /\.(css|scss)$/,
                use: [MiniCssExtractPlugin.loader, "css-loader", "sass-loader"],
            },
            {
                test: /\.(jpg|jpeg|png|gif|mp3|svg)$/,
                use: ["file-loader"],
            },
        ],
    },
    resolve: {
        extensions: ['.tsx', '.ts', '.js']
    },
    optimization: {
        minimize: true,
    },
    plugins: [
        new webpack.ProvidePlugin({
            "React": "react",
        }),
        new ESLintPlugin(),
        new MiniCssExtractPlugin({
            filename: '../css/index.css'
        }),
    ],
};