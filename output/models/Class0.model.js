const mongoose = require('mongoose');

const Class0Schema = new mongoose.Schema({
  sadasd: { type: Number, required: true },
  asdsa: [String]
});

module.exports = mongoose.model('Class0', Class0Schema);
