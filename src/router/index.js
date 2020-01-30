import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/pages/Home'
import Assess from '@/pages/Questionnaire'

Vue.use(Router)

const fields = {
  "pages": [
      {
          "title": "About you",
          "items": [
              {
                  "fieldType": "small-text-input",
                  "name": "name",
                  "label": "Your name"
              },
              {
                  "fieldType": "small-text-input",
                  "name": "carer",
                  "label": "If you're filling this in with a parent or carer, what's their name?"
              }
          ]
      },
      {
          "title": "Technology you own",
          "items": [
              {
                  "fieldType": "multiple-choice-input",
                  "name": "devices",
                  "label": "What devices do you currently own?",
                  "options": [
                      "Smart phone",
                      "Tablet",
                      "Laptop or desktop computer"
                  ]
              }
          ]
      },
      {
          "title": "What topics interest you?",
          "items": [
              {
                  "fieldType": "multiple-choice-input",
                  "name": "topics",
                  "label": "Technology can help to increase independence and improve quality of life. What topics are you interested in finding out more about?",
                  "options": [
                      "Going shopping",
                      "Preparing food",
                      "Working"
                  ]
              }
          ]
      },
      {
          "title": "Going shopping",
          "items": [
              {
                  "fieldType": "boolean-input",
                  "name": "blindorpartially",
                  "label": "Are you blind or partially sighted?"
              },
              {
                  "fieldType": "boolean-input",
                  "name": "wanttoshopalone",
                  "label": "Would you like to go out to the shops more on your own?"
              },
              {
                  "fieldType": "single-choice-input",
                  "name": "shopconfident",
                  "label": "How confident do you feel about going out to the shops on your own?",
                  "options": [
                      "I don't feel confident",
                      "I feel confident when I'm with other people",
                      "I am confident going on my own"
                  ]
              },
              {
                  "fieldType": "single-choice-input",
                  "name": "shopsafe",
                  "label": "How safe do you feel when going to the shops on your own?",
                  "options":[
                      "I don't feel safe at all",
                      "I sometimes feel safe",
                      "I feel safe"
                  ]
              },
              {
                  "fieldType":"boolean-input",
                  "name":"shopforgetitems",
                  "label": "Do you often forget what items you need to buy at the shops?"
              },
              {
                  "fieldType":"boolean-input",
                  "name":"shopforgetroute",
                  "label": "Do you often forget how to get back home?"
              }
          ]
      }
  ]
} 

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
        fields
      }
    }
  ]
})
