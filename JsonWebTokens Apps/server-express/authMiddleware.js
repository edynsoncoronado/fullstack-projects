const jwt = require("jsonwebtoken");
const {expressjwt} = require('express-jwt');

// Configura el secreto para JWT
const secret = "shhhhhhared-secret";

// Crea una función para generar el token
const generateToken = (user) => {
  const payload = {
    id: user.id,
    email: user.email,
    admin: user.admin
  };
  return jwt.sign(payload, secret, { expiresIn: "1h" });
};

// Crea un middleware para validar el token
const validateToken = expressjwt({secret: secret, algorithms: ['HS256']});

module.exports = { generateToken , validateToken};
