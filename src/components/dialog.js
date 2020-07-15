import Dialog from './Dialog.vue'

function Install (Vue, vuetify) {
    const property = '$dialog'
    const Ctor = Vue.extend(Object.assign({ vuetify }, Dialog))

    function createDialogCmp (options) {
      const container = document.querySelector('[data-app=true]') || document.body
      return new Promise(resolve => {
        const cmp = new Ctor(Object.assign({}, {
          propsData: Object.assign({}, options),
          destroyed: () => {
            container.removeChild(cmp.$el)
            resolve(cmp.value)
          }
        }))
        container.appendChild(cmp.$mount().$el)
      })
    }
    
    function show (title, message, buttons, fullscreen = false, options = {}) {
      options.title = title
      options.message = message
      options.buttons = buttons
      options.fullscreen = fullscreen
      return createDialogCmp(options)
    }
  
    Vue.prototype[property] = show  
    Vue.prototype[property].confirm = (title, message) => {return show(title, message, ['OK', 'Cancel'])}
    Vue.prototype[property].fullscreen = (title, message) => {return show(title, message, ['Back'], true)}
  }

  if (typeof window !== 'undefined' && window.Vue) {
    window.Vue.use(Install)
  }
  
  export default Install