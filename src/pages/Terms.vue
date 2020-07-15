<template>
    <v-container>
        <v-card>
            <v-progress-circular id="loading-terms" v-if="loading"></v-progress-circular>
            <div v-else-if="terms" class='text-left'>
                <v-container>
                    <div role="heading" aria-level="3" class="text-h3 mb-2" v-text="terms.title" tabindex="0"></div>
                </v-container>
                <v-divider/>
                <v-container id='terms-content' class='text-left' v-html="terms.content">
                </v-container>
            </div>
            <div v-else>We're sorry, but we're unable to find this at the moment.</div>
        </v-card>
    </v-container>
</template>

<script>
import newTab from '@/js/newTab.js'
export default {
    name: "terms",
    data() {
        return {
            endpoint: process.env.VUE_APP_API_ENDPOINT,
            terms: null,
            loading: true
        }
    },
    created() {
        fetch(this.endpoint + '/config/disclaimer')
        .then(x=>x.json())
        .then(x=>{
            this.terms = {...x, content: newTab(x.content)};
        })
        .catch()
        .finally(()=>this.loading = false)
    }
}
</script>

