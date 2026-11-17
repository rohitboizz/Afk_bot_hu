const mineflayer = require('mineflayer')

function startBot() {
  const bot = mineflayer.createBot({
    host: 'deadlymc.mcsh.gg',
    port: 25565,
    username: 'AfkBot123',
    version: false
  })

  bot.on('login', () => {
    console.log('Bot join ho gaya!')
  })

  bot.on('spawn', () => {
    console.log('Bot spawn ho gaya, ab AFK rahega')
    // Har 20 sec me halka jump taaki kick na lage
    setInterval(() => {
      bot.setControlState('jump', true)
      setTimeout(() => bot.setControlState('jump', false), 500)
    }, 20000)
  })

  bot.on('kicked', (reason) => {
    console.log('Kick hua:', reason)
    setTimeout(startBot, 5000)
  })

  bot.on('error', (err) => console.log(err))
  bot.on('end', () => setTimeout(startBot, 5000))
}

startBot()
