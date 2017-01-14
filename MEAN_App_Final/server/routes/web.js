var express = require('express');
router = express.Router();
path = require("path");

router.get('/', function (req, res, next) {
    res.sendFile(absPath + "/app.html");
});

module.exports = router;