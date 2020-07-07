import Vue from 'vue';
import Vuetify from 'vuetify/lib';

Vue.use(Vuetify);

import 'vuetify/dist/vuetify.min.css';
import Dialog from '@/components/dialog.js';

Vue.use(Dialog, vuetify)

let vuetify = new Vuetify();

export default vuetify
