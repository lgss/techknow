<template>
    <v-app-bar app class="primary darken-1">
        <v-container fluid>
            <v-col class="d-flex justify-center">
                <a href="/" style="text-decoration:none">
                    <v-toolbar-title class="white--text">
                        <b>{{ title }}</b>
                    </v-toolbar-title>
                </a>
            </v-col>
        </v-container>
    </v-app-bar>
</template>

<script>
export default {
    props: ["title"]
};
</script>
