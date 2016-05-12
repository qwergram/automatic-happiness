describe('test comments show up', function() {

  it('sanity test', function() {
    expect(1).toEqual(1);
  });

  it('has the right title', function() {
    browser.get('test');
    bad_url = browser.getCurrentUrl();
  });

});
