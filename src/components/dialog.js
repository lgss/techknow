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
    
    function show (title, message, buttons, options = {}) {
      options.title = title
      options.message = message
      options.buttons = buttons
      return createDialogCmp(options)
    }
  
    Vue.prototype[property] = show
  }

  if (typeof window !== 'undefined' && window.Vue) {
    window.Vue.use(Install)
  }
  
  export default Install