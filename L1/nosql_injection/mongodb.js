const express = require('express')
const app = express()
const mongoose = require('mongoose')
const db = mongoose.connection

mongoose.connect('mongodb://localhost:27017/', { userNewUrlParser: true, useUnifiedTopology: true })
app.get('/query', (req, res) => {
    db.collection('user').find({
        'uid': req.query.uid,
        'upw': req.query.upw
    }).toArray((err, result) => {
        if (err) throw err
        res.send(result)
    })
})

const server = app.listen(3000, () => {
    console.log('app.listen')
})

// 아 걍 서버 실제로 돌리진 않을게요