$(document).ready(function(){
    $('.footer-distributed').css('margin-top', $(document).height() - ( $('.contentofpage').height() + $('.footer-distributed').height()) - 50 );
});

// So we are extending the size of the document by making the final height of the document = height of the window + 50 px by adding a big margin-top to the footer element.
// Hence the footer will always remain stuck to the bottom
// $(window).height() gets you an unit-less pixel value of the height of the (browser) window aka viewport. With respect to the web browsers the viewport here is visible portion of the canvas(which many times is smaller than the document being rendered).
//$(document).height() returns an unit-less pixel value of the height of the document being rendered. If the actual document’s body height is less than the viewport height then it will return the viewport height instead.