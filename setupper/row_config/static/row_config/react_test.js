function room_data(name, row) {
    this.name = name
    this.row_top = row
    this.row_bottom = row
}

var room_names = ['1315', '1325', '1400', '1410', '1415', '1420', '1425', '1430', '1400-1410', '1420-1430', '1400-1430'];

var rooms = [];

for (var i = 0; i < room_names.length; i++) {
    rooms.push(room_data(room_names[i], i));
}
