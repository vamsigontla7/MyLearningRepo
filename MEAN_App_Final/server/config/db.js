var mongoose = require('mongoose');
mongoose.Promise = global.Promise;
var connection = mongoose.connect('mongodb://localhost/mean_db_final');
module.exports = connection;