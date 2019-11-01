const webpack = require('webpack');
// Initialize doteenv library
require('dotenv').config();
const withCSS = require('@zeit/next-css');

module.exports = {
    webpack: config => {
        //CSS Loaders
        config.resolve.extensions = ['.js', '.jsx', '.css'];
        config.module.rules.push(
            { test: /\.css$/, loader: 'style-loader!css-loader' },
            { test: /\.png$/, loader: 'url-loader?limit=100000' },
            { test: /\.jpg$/, loader: 'file-loader' },
        );
        // Fixes npm packages that depend on `fs` module
        config.node = {
            fs: 'empty',
        };
        /**
         * Returns environment variables as an object
         */
        const env = Object.keys(process.env).reduce((acc, curr) => {
            acc[`process.env.${curr}`] = JSON.stringify(process.env[curr]);
            return acc;
        }, {});

        /** Allows you to create global constants which can be configured
         * at compile time, which in our case is our environment variables
         */
        config.plugins.push(new webpack.DefinePlugin(env));
        return config;
    },
};
module.export = withCSS({
    cssModules: false,
    cssLoaderOptions: {
        url: false,
    },
    webpack: config => {
        // const config = {};

        config.plugins = config.plugins || [];

        config.plugins = [
            ...config.plugins,
            // Read the .env file
            new Dotenv({
                path: path.join(__dirname, '.env'),
                systemvars: true,
            }),
        ];

        config.node = {
            fs: 'empty',
        };
        /**
         * Returns environment variables as an object
         */
        const env = Object.keys(process.env).reduce((acc, curr) => {
            acc[`process.env.${curr}`] = JSON.stringify(process.env[curr]);
            return acc;
        }, {});

        /** Allows you to create global constants which can be configured
         * at compile time, which in our case is our environment variables
         */
        config.plugins.push(new webpack.DefinePlugin(env));
        return config;
    },
});