describe('test comments show up', function() {

  it('contains a div#content tag', function() {
    browser.get('/');
    expect(browser.getTitle()).toEqual('React Tutorial');
  });

});
