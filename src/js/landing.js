// this is a bit of a hack because I don't want to use Vuex for one thing
let content = ''
exports.get = () => content
exports.set = (value) => content = value