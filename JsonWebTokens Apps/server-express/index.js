const express = require("express");
const { generateToken, validateToken } = require("./authMiddleware");

const app = express();

app.post("/api/auth/token", (req, res) => {
  const user = { id: 1, email: "usuario@example.com", admin:true };

  // Genera el token
  const token = generateToken(user);

  // Envía el token en la respuesta
  res.json({ token });
});

app.get('/api/users', validateToken, (req, res) => {
  console.log(req.auth);
  //validando que el usuario sea admin
  if(req.auth.admin){
    return res.status(200).send('Data Protected')
  }
  //respuesta para el usuario que no es admin
  res.status(401).send({ message: 'not authorized' })
})

app.get("/", (req, res) => {
  res.send("Hola mundo22");
});

app.listen(3000, () => {
  console.log("Aplicación iniciada en el puerto 3000");
});
