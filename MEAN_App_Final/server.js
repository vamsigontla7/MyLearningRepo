var express = require('express');

path = require('path');
bodyParser = require('body-parser');

routes = require('./server/routes/web');
apiRoutes = require('./server/routes/api');
connection = require('./server/config/db');

var app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, 'app')));
app.use(express.static('node_modules'));
app.use('/', routes);
app.use('/api', apiRoutes);

var port = process.env.port || 3000;
app.listen(port, function () {
    console.log("Server is running at : http://localhost:" + port);
});