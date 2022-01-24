const bears = {}
chrome.runtime.onMessage.addListener(function(request,sender,sendResponse){
    bears[request.url] = request.count

})