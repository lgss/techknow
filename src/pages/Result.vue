<template>
  <v-simple-table>
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">Name</th>
          <th class="text-left">Content</th>
          <th class="text-left">Tags</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="resource in results.resources.filter(resource => checkTags(answers, resource.tags))" :key="resource.name">
          <td class="text-left">{{ resource.name }}</td>
          <td class="text-left">{{ resource.content }}</td>
          <td class="text-left">{{ resource.tags }}</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
</template>

<script>
export default {
    name: 'Result',
    components: {},
    props: ["results", "answers"],
    methods: {
      checkTags(answers, tags) {
        return tags.some(resourceTag => this.getAnswerTags(answers).some(answerTag => answerTag == resourceTag))
      },
      getAnswerTags(answers) {
        let tags = []
        answers.forEach(answer => {
            answer.options.forEach( option => {
              option.tags.forEach(tag => {
                tags.push(tag)
              })
            })
        })
        return tags
      }
    },
    data(){
        return {}
    }
}
</script>

<style>

</style>