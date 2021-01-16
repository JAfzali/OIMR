<template>
  <div class="rackloc">
    <v-container grid-list-xl  >
      <v-layout row wrap>
        <v-flex md12>
          <v-card height="558px" raised flat tile>
            <v-tabs
              v-model="tab"
              background-color="white"
              centered
              grow
              >
              <v-tab
                v-for="(rack, key) in getracksAndPipes"
                :key="key"
                >
                {{ key }}
              </v-tab>
            </v-tabs>
            <v-tabs-items v-model="tab">
               <v-tab-item
                v-for="(rack, key) in getracksAndPipes"
                :key="key"
                >
                  <v-card>
                    <table>
                      <tr
                      v-for="list in rack"
                      :key="list"
                      >
                        <td
                          v-for="pipe in list"
                          :key="pipe.Serial_Number"
                          >
                          <v-btn v-if="getDateDiff(pipe) < 17" color="green" fab x-small
                          v-on:click="setInfo(pipe,'green')"
                          >
                            <span class="black--text ">{{pipe.Position}}</span>
                          </v-btn>
                          <v-btn v-else-if="getDateDiff(pipe) < 62 & getDateDiff(pipe) >= 18" color="yellow" fab x-small
                          v-on:click="setInfo(pipe,'yellow')"
                          >
                            <span class="black--text ">{{pipe.Position}}</span>
                          </v-btn>
                          <v-btn v-else fab x-small color="red"
                          v-on:click="setInfo(pipe,'red')"
                          >
                            <span class="black--text ">{{pipe.Position}}</span>
                          </v-btn>
                        </td>
                      </tr>
                    </table>
                  </v-card>
               </v-tab-item>
             </v-tabs-items>
          </v-card>
        </v-flex>
      </v-layout >
    </v-container>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import moment from 'moment'
export default {
  name: 'racklocation',
  props: {
    btncolor: {
      type: String,
      default: 'blue'
    }
  },
  data () {
    return {
      admins: [
        ['control_point'],
        ['location_on']
      ],
      items: [
        { tab: 'Rack 01 A', content: 'første' },
        { tab: 'Rack 01 B', content: 'andre' },
        { tab: 'Rack 02 A', content: 'tredje' },
        { tab: 'Rack 02 B', content: 'fjerde' }
      ],
      tab: null,
      rackinfo: 'Click one of the pipes for more details ',
      test: 'test',
      serialnr: '',
      position: '',
      itemnr: '',
      antall: '',
      disable: true,
      insp_date: '',
      description: '',
      ordernr: ''
    }
  },
  computed: {
    ...mapGetters([
      'getUsername', 'getracksAndPipes'
    ]),
    getCards () {
      const infocard = [
        { headline: 'Serial Number', val: this.serialnr, icon: 'info' },
        { headline: 'Item Number', val: this.itemnr, icon: 'info' },
        { headline: 'Inspection Date', val: this.insp_date, icon: 'event' },
        { headline: 'Description', val: this.description, icon: 'description' },
        { headline: 'Order Number', val: this.ordernr, icon: 'info' }
      ]
      return infocard
    },
    cssProps () {
      return {
        '--secondary-color': this.$vuetify.theme.secondary
      }
    }
  },
  created: function () {
    this.fetchracksAndPipes()
  },
  methods: {
    ...mapActions(['fetchracksAndPipes']),
    setInfo: function (pipe, color) {
      this.disable = false
      this.rackinfo = ''
      this.serialnr = pipe.Serial_Number
      this.rackpos = pipe.Rack_Position
      this.position = pipe.Position
      this.itemnr = pipe.Item_No
      this.insp_date = pipe.Date_Inspected
      this.description = pipe.Description
      this.ordernr = pipe.Order_No
    },
    testmethod: function (par) {
      console.log('test')
    },
    getDateDiff: function (pipe) {
      var now = moment(new Date())
      var end = moment(pipe.Date_Inspected)
      var duration = moment.duration(now.diff(end))
      var days = duration.asDays()
      console.log(days)
      return days
    }
  }
}
</script>

<style lang="css" scoped>
.v-btn{
    margin:15px;
}
#bigbtn {
  background-color: var(--secondary-color);
}
table { margin: auto; }

table, tr, td {
  border: 1px solid black;
}

.v-card {
  overflow-y:auto;
}

</style>
