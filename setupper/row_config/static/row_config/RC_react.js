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

var Slider = React.createClass({
    render: function() {
        var room = this.props.room;
        var position = room.fields.row_top * rowHeight; 
        var sliderLength = ((room.fields.row_bottom + 1) - room.fields.row_top) * rowHeight;
        return (
            React.createElement('td', {
                className: 'slide_cell', 
                height: this.props.height.toString() + 'px',
                key: this.props.key }, 
                React.createElement('div', {
                    className: 'slider', 
                    id: 'slider' + this.props.index.toString(),
                    style: {
                        height: sliderLength.toString() + 'px',
                        transform: 'translateY(' + position + 'px)', 
                        WebkitTransform: 'translateY('+ position + 'px)'
                        },
                    key: this.props.key }, 
                    room.fields.row_top 
                )
            )
        )
    }

});

var SliderBox = React.createClass({
    render: function() {
        var cols = [];
        var height = this.props.rooms.length * rowHeight;
        this.props.rooms.forEach(function(room, index) {
            cols.push(
                React.createElement(Slider, {
                    room: room, 
                    index: index,
                    key: index, 
                    height: height}, {})
            );
        });
        return (React.createElement('tr', {}, cols))
    }
});

var RowTable = React.createClass({
    getInitialState: function() {
        return {rooms: this.props.rooms};
    },
    render: function() {
        return (
            React.createElement('table', {}, 
      	    React.createElement('tbody', {},
      	        React.createElement(RowHeadings, {rooms: this.state.rooms}, {}),
                React.createElement(SliderBox, {rooms: this.state.rooms}, {})
                )
            )
        );
    }
});



