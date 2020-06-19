<template>
  <div>
    <journey/>
    <v-skeleton-loader v-show="loading" type="card"/>
    <v-card v-show="!loading && !showJourneys">
      <h1>How can we help you today?</h1>
      <v-item-group multiple class="pa-5" model="sel">
        <v-row>
          <v-col v-for="(cat, index) in categories" :key="'c-' + index" cols="12" md="4">
            <v-item v-slot:default="{ active, toggle }" :value="'c-' + index">
                <v-card 
                  :color="active ? 'primary' : 'grey lighten-3'"
                  class="d-flex align-center"
                  height="200"
                  @click="toggle(); cat.selected = !active"
                >
                  <span class="display-3 flex-grow-1 text-center">{{cat.name}}</span>
                </v-card>
            </v-item>
          </v-col>
        </v-row>
      </v-item-group>
      <v-row center>
        <v-col>
          <v-btn @click="categoriesSelected=true">Continue</v-btn>
        </v-col>
      </v-row>
    </v-card>
    <v-card v-show="!loading && showJourneys">
      <h1>How can we help you today?</h1>
      <v-item-group multiple class="pa-5" model="selj">
        <v-row>
          <v-col v-for="(journey, index) in possibleJourneys" :key="'j-' + index" cols="12" md="4">
            <v-item v-slot:default="{ active, toggle }" :value="'j-' + index">
              <!-- <journey/> -->
                <v-card 
                  :color="active ? 'primary' : 'grey lighten-3'"
                  class="d-flex align-center justify-left"
                  height="100"
                  :value="index"
                  @click="toggle(); journey.selected = !active"
                > <v-container>
                  <v-img
                    contain
                    :alt="journey.image ? journey.image.alt : null"
                    :src="journey.image ? journey.image.src : undefined"
                    max-height=100
                    lazy-src="https://via.placeholder.com/251">
                  </v-img>
                  <span class="display-1 flex-grow-1 text-center">{{journey.label}}</span>
                  </v-container>
                </v-card>
            </v-item>
          </v-col>
        </v-row>
      </v-item-group>
      <v-row center>
        <v-col>
          <v-btn @click="categoriesSelected=false">Back</v-btn>
          <v-btn color="success" @click="beginAssessment">Begin</v-btn>
        </v-col>
      </v-row>
    </v-card>
  </div>
</template>

<script>
import landing from '@/js/landing.js'
import Journey from '@/components/Journey.vue'

export default {
  components: {
    Journey
  },
  name: "Selection",
  created() {
    fetch(this.endpoint + '/journeys')
      .then(x => x.json())
      .then(x => {
        this.journeys = x
        let uniqueParents = Array.from(new Set(x.map(journey => {return journey.parent})))
        this.categories = uniqueParents.map( parent => {return{"name":parent,"selected":false}})
        this.loading = false
      })
  },
  computed: {
    showJourneys() {
      return this.categoriesSelected || this.categories.length <= 1
    },
    selectedCats() {
      return this.categories.filter(x => x.selected).map(x => x.name)
    },
    possibleJourneys() {
      if (this.categories.length <= 1 || this.selectedCats.length === 0)
        return this.journeys

      return this.journeys.filter(x => this.selectedCats.indexOf(x.parent) >= 0)
    },
    selectedJourneys() {
      if (this.possibleJourneys.length <= 1)
        return this.possibleJourneys

      return this.possibleJourneys.filter(x => x.selected).map(x => x.id)
    }
  },
  methods: {
    beginAssessment() {
      this.$router.push({"name": "Assessment", params: {journeys: this.selectedJourneys}})
    }
  },
  data() {
    return {
      selc: [],
      selj: [],
      primaryColour: landing.get(),
      loading: true,
      categoriesSelected: false,
      endpoint: process.env.VUE_APP_API_ENDPOINT,
      categories: [],
      categories2: [],
      journeys: []
    }
  }
}
</script>