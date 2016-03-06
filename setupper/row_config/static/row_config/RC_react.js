var rowHeight = 40;

var RowHeadings = React.createClass({
    render: function() {
    var headings = [];
    this.props.rooms.forEach(function(room) {
    	headings.push(React.createElement('th', {key: room.pk}, room.fields.name));
    });
  	return (React.createElement('tr', {}, headings));
  }
});

var SlideColumns = React.createClass({
    render: function() {
        var cols = [];
        var height = this.props.rooms.length * rowHeight;
        this.props.rooms.forEach(function(room, index) {
            var position = room.fields.row_top * rowHeight;
            cols.push(
                React.createElement('td', {
                    className: 'slide_cell', 
                    height: height.toString() + 'px',
                    key: index }, 
                    React.createElement('div', {
                        className: 'slider', 
                        style: {
                            transform: 'translateY(' + position + 'px)', 
                            WebkitTransform: 'translateY('+ position + 'px)'
                            },
                        key: index }, 
                        room.fields.row_top 
                    )
                )
            );
        });
        return (React.createElement('tr', {}, cols))
    }
});

var RowTable = React.createClass({
  render: function() {
    return (
      React.createElement('table', {}, 
      	React.createElement('tbody', {},
      	    React.createElement(RowHeadings, {rooms: this.props.rooms}, {}),
            React.createElement(SlideColumns, {rooms: this.props.rooms}, {})
        )
      )
    );
  }
});


// Interact
var snapSettings = {
	targets: [ 
            interact.createSnapGrid({ x: 40, y: 40 }) 
        ],
  range: Infinity,
}

interact('.slider')
    .draggable({
        snap: snapSettings, 
        autoscroll: true, 
        onmove: dragMoveListener
    })

function dragMoveListener(event) {
    var target = event.target;

}
