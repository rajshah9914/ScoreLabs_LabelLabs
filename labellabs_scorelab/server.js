// // const path = require("path");
// // const multer = require("multer");

// // const storage = multer.diskStorage({
// //    destination: "./public/uploads/",
// //    filename: function(req, file, cb){
// //       cb(null,"IMAGE-" + Date.now() + path.extname(file.originalname));
// //    }
// // });

// // const upload = multer({
// //    storage: storage,
// //    limits:{fileSize: 1000000},
// // }).single("myImage");
// // const router = express.Router();
// // router.post("/upload", {
// //    upload(req, res, (err) => {
// //       console.log("Request ---", req.body);
// //       console.log("Request file ---", req.file);//Here you get file.
// //       /*Now do where ever you want to do*/
// //       if(!err)
// //          return res.send(200).end();
// //    });
// // };);


// const express = require('express');
// const bodyParser = require('body-parser');
// const app = express();
// const port = process.env.PORT || 5000;
// app.use(bodyParser.json());
// app.use(bodyParser.urlencoded({ extended: true }));

// app.get('/api/hello', (req, res) => {
//   res.send({ express: 'Hello From Express' });
// });
// app.post('/api/world', (req, res) => {
//   console.log(req.body);
//   res.send(
//     `I received your POST request. This is what you sent me: ${req.body.post}`,
//   );
// });

// app.listen(port, () => console.log(`Listening on port ${port}`));