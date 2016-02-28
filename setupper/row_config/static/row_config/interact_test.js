// target elements with the "slider" class
var snapGrid = interact.createSnapGrid({ x: 20, y: 40 })

var snapSettings = {
	targets: [ interact.createSnapGrid({ x: 100, y: 40 }) ],
  range: Infinity,
}

interact('.slider')
    .draggable({
        // enable inertial throwing
        inertia: false,
        // keep the element within the area of it's parent
        snap: snapSettings,
        // enable autoScroll
        autoScroll: true,
        // call this function on every dragmove event
        onmove: dragMoveListener,
    })
    .resizable({
        snap: snapSettings,
        edges: { left: false, right: false, bottom: true, top: false }
    })
    .on('resizemove', resizeListener)
  
function resizeListener(event) {
    var target = event.target,
    y = (parseFloat(target.getAttribute('data-y')) || 0);

    target.style.height = event.rect.height + 'px';

    target.style.webkitTransform = 
        target.style.transform =
        'translate(0px, ' + y + 'px)';

    target.setAttribute('data-y', y);
  }

function dragMoveListener (event) {
    var target = event.target,
    // keep the dragged position in the data-y attributes
    y = (parseFloat(target.getAttribute('data-y')) || 0) + event.dy;

    // translate the element
    target.style.webkitTransform =
    target.style.transform =
      'translate(0px, ' + y + 'px)';

    // update the posiion attributes
    // target.setAttribute('data-x', x);
    target.setAttribute('data-y', y);
  }

function room_data(name, row) {
    this.name = name
    this.row_top = row
    this.row_bottom = row
}

var room_names = ['1315', '1325', '1400', '1410', '1415', '1420', '1425', '1430', '1400-1410', '1420-1430', '1400-1430']

for (var i = 0; i < room_names.length; i++)

