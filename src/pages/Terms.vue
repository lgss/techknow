<template>
    <v-container>
        <v-card>
            <v-progress-circular id="loading-terms" v-if="loading"></v-progress-circular>
            <div v-else-if="terms">
                <v-container>
                    <div role="heading" aria-level="3" class="text-h4 mb-2" v-text="terms.title" tabindex="0"></div>
                </v-container>
                <v-divider/>
                <v-container id="terms-content" v-html="terms.content">
                </v-container>
            </div>
            <div v-else>We're sorry, something's gone wrong. Please try again later.</div>
        </v-card>
    </v-container>
</template>

<script>
export default {
    name: "terms",
    data() {
        return {
            endpoint: process.env.VUE_APP_API_ENDPOINT,
            loading: false
        }
    },
    computed: {
        terms() {
            return this.$store.getters.staticContent("DISCLAIMER")
        }
    }
}
</script>

