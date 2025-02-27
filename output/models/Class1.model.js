const mongoose = require('mongoose');

const Class1Schema = new mongoose.Schema({
  asdd: { type: mongoose.Schema.Types.ObjectId, ref: 'Class0' }
});

module.exports = mongoose.model('Class1', Class1Schema);
