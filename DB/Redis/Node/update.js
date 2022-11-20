const {createClient} = require("redis");
const client = createClient('redis://localhost:6379');

client.connect();

(async () => {
    await client.set('key', 'new value');
    client.disconnect();
})();