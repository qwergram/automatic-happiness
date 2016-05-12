exports.config = {
  specs: ['tutorial.js'],
  capabilities: {
    browserName: 'chrome'
  },
  baseUrl: 'http://127.0.0.1:3000',
  seleniumAddress: 'http://127.0.0.1:4444/wd/hub',
  framework: 'jasmine',
}
