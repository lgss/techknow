export default {
      intersects(one, two) {
        return one && two && (one.some(element => two.includes(element)))
      },
      getResponseTags(responses) {
        return (responses || []).flatMap(x => x.choices).flatMap(x => x.tags)
      }
}