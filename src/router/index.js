import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/pages/Home'
import Assess from '@/pages/Assess'
import Result from '@/pages/Result'
import Select from '@/pages/Select'

Vue.use(Router)


export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/assess',
      name: 'Assessment',
      props: true,
      component: Assess
    },
    {
      path: '/select',
      name: 'Select',
      component: Select
    },
    {
      path: '/result',
      name: 'Result',
      component: Result,
      props: true
    }
  ]
})
