const express = require('express');
const redis = require('redis');

const client = redis.createClient();
client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('ready', () => console.log('Redis client connected to the server'));

const app = express();
app.use(express.json());
const port = 1245;

const listProducts = [
  {
    id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4
  },
  {
    id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10
  },
  {
    id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2
  },
  {
    id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5
  },
];

function getItemById(id) {
  return listProducts.find(item => item.id === id.toString());
};

function reserveStockById(itemId, stock) {
  const item = getItemById(itemId);
  if (item === undefined) {
    return 0;
  } else {
    const newStock = (item.stock - stock);
    if (newStock < 1) {
      return -1;
    } else {
      client.set(item.stock, newStock, redis.print);
      return 1;
    }
  }
};

async function getCurrentReservedStockById(itemId) {
  const item = getItemById(itemId);
  if (item === undefined) {
    return { status: 'Product not found' };
  } else {
    await client.get(item.stock, (err, data) => (data));
  }
};

app.get('/list_products', (req, res) => {
  res.send(JSON.stringify(listProducts));
  res.end();
});

app.get('/list_products/:itemId', async (req, res) => {
  res.send(JSON.stringify(await getCurrentReservedStockById(req.params.itemId)));
  res.end()
});

app.get('/reserve_product/:itemId', (req, res) => {
  const status = reserveStockById(req.params.itemId, 1);
  switch (status) {
    case -1:
      res.send(JSON.stringify({ status: 'Not enough stock available', itemId: req.params.itemId }));
      break;
    case 0:
      res.send(JSON.stringify({ status: 'Product not found' }));
      break;
    case 1:
      res.send(JSON.stringify({ status: 'Reservation confirmed', itemId: req.params.itemId }));
  }
  res.end();
})

app.listen(port, () => {
  console.log(`server is running at ${port}`);
});
