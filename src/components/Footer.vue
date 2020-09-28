<template>
    <v-footer color="secondary" class="justify-center">
        <v-card flat tile color="secondary">
            <v-card-text>
                <v-row
                    justify="center"
                >
                    <v-col
                        class="text-center"
                        cols="auto"
                    >
                        <router-link class="white--text" to='/Terms' target="_blank">
                            Terms and Conditions
                        </router-link>
                    </v-col>
                    <v-col
                        class="text-center"
                        cols="auto"
                    >
                        <router-link class="white--text" to='/Accessibility' target="_blank">
                            Accessibility statement
                        </router-link>
                    </v-col>
                </v-row>
            </v-card-text>
        </v-card>
    </v-footer>
</template>
