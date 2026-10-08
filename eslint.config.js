// Flat config - evaluated at eslint startup.
const os = require('os');
module.exports = [
  {
    rules: {},
    // fixture marker: one synthetic diagnostic carrying a runtime-unique id
    settings: { vendorBuild: `v4-${process.pid}` },
  },
];
