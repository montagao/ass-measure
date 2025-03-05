// index.js
const { measureDimensions } = require('./build/Release/assaddon.node');

module.exports = (assFilePath, width, height) => {
  if (typeof assFilePath !== 'string' || typeof width !== 'number' || typeof height !== 'number') {
    throw new Error('Invalid parameters provided.');
  }
  return measureDimensions(assFilePath, width, height);
};

