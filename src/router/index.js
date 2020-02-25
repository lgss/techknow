import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/pages/Home'
import Assess from '@/pages/Assess'
import Result from '@/pages/Result'

const fields = require('../../static/assess.json');
const responses =[];

Vue.use(Router)

const resources =  require('../../static/resource.json');

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
      component: Assess,
      props: {
        fields,
        responses
      }
    },
    {
      path: '/result',
      name: 'Result',
      component: Result,
      props: {
        resources,
        responses
      }
    }
  ]
})
