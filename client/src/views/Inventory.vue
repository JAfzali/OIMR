<template>
  <v-container fluid>
    <v-row justify="center">
      <v-dialog
        v-model="dialog3"
        fullscreen
        hide-overlay
        transition="dialog-bottom-transition"
      >
        <v-card>
          <v-toolbar dense color="white">
            <v-btn icon @click="clearList">
              <v-icon>mdi-close</v-icon>
            </v-btn>
            <v-spacer></v-spacer>
            <v-toolbar-title
              ><b>{{ Itemnr }}</b></v-toolbar-title
            >
            <v-spacer></v-spacer>
          </v-toolbar>
          <v-divider></v-divider>
          <v-card-title>
            {{ location }}
            <v-spacer></v-spacer>
            <v-text-field
              v-model="search2"
              append-icon="mdi-magnify"
              label="Search"
              single-line
              hide-details
            ></v-text-field>
          </v-card-title>
          <v-data-table
            :loading="pipeload"
            :headers="headers3"
            :items="numbers"
            :search="search2"
          >
          <template v-slot:item.Serial_Number="{ item }">
              <v-tooltip right>
                <template v-slot:activator="{ on }">
                  <v-btn
                    width="90"
                    v-on="on"
                    small
                    color="white"
                    @click="showRack(item)"
                    >{{ item.Serial_Number }}<v-spacer></v-spacer
                  ></v-btn>
                </template>
                <span>Show Rack</span>
              </v-tooltip>
            </template>
          </v-data-table>
        </v-card>
      </v-dialog>
      <v-dialog
        v-model="dialog"
        fullscreen
        hide-overlay
        transition="dialog-bottom-transition"
      >
        <v-card>
          <v-toolbar dense color="white">
            <v-btn icon @click="clearList">
              <v-icon>mdi-close</v-icon>
            </v-btn>
            <v-spacer></v-spacer>
            <v-toolbar-title
              ><b>{{ Itemnr }}</b></v-toolbar-title
            >
            <v-spacer></v-spacer>
          </v-toolbar>
          <v-divider></v-divider>
          <v-card-title>
            Rig Ready
            <v-spacer></v-spacer>
            <v-text-field
              v-model="search2"
              append-icon="mdi-magnify"
              label="Search"
              single-line
              hide-details
            ></v-text-field>
          </v-card-title>
          <v-data-table
            :loading="pipeload"
            :headers="headers2"
            :items="numbers"
            :search="search2"
          >
            <template v-slot:item.Serial_Number="{ item }">
              <v-tooltip right>
                <template v-slot:activator="{ on }">
                  <v-btn
                    width="90"
                    v-on="on"
                    small
                    color="white"
                    @click="showRack(item)"
                    >{{ item.Serial_Number }}<v-spacer></v-spacer
                  ></v-btn>
                </template>
                <span>Show Rack</span>
              </v-tooltip>
            </template>
          </v-data-table>
        </v-card>
      </v-dialog>
      <v-dialog v-model="dialog2" fullscreen>
        <v-card>
          <v-toolbar dense color="white">
            <v-btn icon @click="clearRack">
              <v-icon>mdi-close</v-icon>
            </v-btn>
            <v-spacer></v-spacer>
            <v-toolbar-title>{{ Serialnr }}</v-toolbar-title>
            <v-spacer></v-spacer>
          </v-toolbar>
          <div>
            <v-container fluid>
              <v-row>
                <v-col
                  ><v-card :min-height="header_min_height" dark color="#748cab">
                    <v-card-subtitle class="text-left text-subtitle-1"
                      >Site</v-card-subtitle
                    >
                    <v-card-title class="text-left text-h4">{{
                      rackinfo.Site
                    }}</v-card-title>
                  </v-card>
                </v-col>
                <v-col
                  ><v-card :min-height="header_min_height" dark color="#3e5c76" >
                    <v-card-subtitle class="text-left text-subtitle-1"
                      >Rack</v-card-subtitle
                    >
                    <v-card-title class="text-left text-h4">{{
                      rackinfo.Rack_ID
                    }}</v-card-title>
                  </v-card>
                </v-col>
                <v-col>
                  <v-card :min-height="header_min_height" dark color="#1d2d44">
                    <v-row dense style="padding-top: 0; padding-bottom: 0;">
                      <v-col style="padding-top: 0; padding-bottom: 0;">
                        <v-card-subtitle class="text-left text-subtitle-1">
                          Item Number
                        </v-card-subtitle>
                      </v-col>
                      <v-col style="padding-top: 0; padding-bottom: 0;">
                        <v-card-subtitle
                          v-for="(key, value) in colormap"
                          :key="value"
                          class="text-left"
                        >
                          <v-tooltip bottom>
                            <template v-slot:activator="{ on }">
                              <v-icon v-on="on" medium color="black">
                                info
                              </v-icon>
                            </template>
                            <br/>
                            <div class="tooltippen" v-for="(key1,value1) in key.iteminfo" :key="key1" >
                              <b>{{value1}}:</b> {{key1}}
                            </div>
                          </v-tooltip>
                          <span style="color: #204060">{{ value }}</span>
                          <v-icon small :style="{ color: computeColor(value) }">
                            brightness_1
                          </v-icon>
                        </v-card-subtitle>
                      </v-col>
                    </v-row>
                  </v-card>
                </v-col>
              </v-row>
            </v-container>
            <v-row>
              <table>
                <tr v-for="list in divideRows" :key="list">
                  <td
                    :style="{ backgroundColor: computeColor(pipe.Item_No) }"
                    class="tdclass"
                    v-for="pipe in list"
                    :key="pipe"
                  >
                    <v-tooltip bottom>
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn
                          v-if="getDateDiff(pipe) < 180"
                          v-bind="attrs"
                          v-on="on"
                          color="green"
                          fab
                          small
                        >
                          <span
                            v-if="pipe.Serial_Number === Serialnr"
                            class="white--text "
                            ><b>{{ pipe.Position }}</b></span
                          >
                          <span v-else class="black--text ">{{
                            pipe.Position
                          }}</span>
                        </v-btn>
                        <v-btn
                          v-else-if="
                            (getDateDiff(pipe) < 365) &
                              (getDateDiff(pipe) >= 181)
                          "
                          v-bind="attrs"
                          v-on="on"
                          color="yellow"
                          fab
                          small
                        >
                          <span
                            v-if="pipe.Serial_Number === Serialnr"
                            class="white--text "
                            ><b>{{ pipe.Position }}</b></span
                          >
                          <span v-else class="black--text ">{{
                            pipe.Position
                          }}</span>
                        </v-btn>
                        <v-btn v-else v-on="on" color="red" fab small>
                          <span
                            v-if="pipe.Serial_Number === Serialnr"
                            class="white--text "
                            ><b>{{ pipe.Position }}</b></span
                          >
                          <span v-else class="black--text ">{{
                            pipe.Position
                          }}</span>
                        </v-btn>
                      </template>
                      <h1>
                        <b>{{ pipe.Position }}</b>
                      </h1>
                      <br />
                      <div><b>Serial Number:</b> {{ pipe.Serial_Number }}</div>
                      <div><b>Item Number:</b> {{ pipe.Item_No }}</div>
                      <div>
                        <b>Inspection Date:</b> {{ pipe.Date_Inspected }}
                      </div>
                      <div><b>Description:</b> {{ pipe.Description }}</div>
                    </v-tooltip>
                  </td>
                </tr>
              </table>
            </v-row>
          </div>
        </v-card>
      </v-dialog>
    </v-row>
    <v-card>
      <v-card-title>
        Inventory Overview
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>
      <v-data-table
        :loading="test"
        :headers="headers"
        :items="filterItems"
        :search="search"
      >
        <template v-slot:item.action="{ item }">
          <v-btn dark small color="black" @click="getPDF(item)">
            PDF
          </v-btn>
        </template>

        <template v-slot:item.Rig_Ready="{ item }">
          <v-tooltip left :disabled="item.Rig_Ready == 0">
            <template v-slot:activator="{ on }">
              <v-btn  v-if="item.Rig_Ready != 0" v-on="on" small text @click="showPipes(item)">{{
                item.Rig_Ready
              }}</v-btn>
              <v-btn v-else v-on="on" small text>{{
                  0
                }}</v-btn>
            </template>
            <span v-if="item.Rig_Ready != 0">Show Pipes</span>
          </v-tooltip>
        </template>

        <template v-slot:item.Scrap="{ item }">
          <v-tooltip left :disabled="item.Scrap == 0">
            <template v-slot:activator="{ on }">
              <v-btn
                v-if="item.Scrap != 0"
                v-on="on"
                small
                text
                @click="showOtherPipes(item, 'Scrap')"
                >{{ item.Scrap }}</v-btn
              >
              <v-btn v-else v-on="on" small text>{{
                0
              }}</v-btn>
            </template>
            <span v-if="item.Scrap != 0">Show Pipes</span>
          </v-tooltip>
        </template>

        <template v-slot:item.Limited_Service="{ item }">
          <v-tooltip left :disabled="item.Limited_Service == 0">
            <template v-slot:activator="{ on }">
              <v-btn
                v-if="item.Limited_Service != 0"
                v-on="on"
                small
                text
                @click="showOtherPipes(item, 'Limited Service')"
                >{{ item.Limited_Service }}</v-btn
              >
              <v-btn v-else v-on="on" small text>{{
                0
              }}</v-btn>
            </template>
            <span v-if="item.Limited_Service != 0">Show Pipes</span>
          </v-tooltip>
        </template>

        <template v-slot:item.Inspection="{ item }">
          <v-tooltip left :disabled="item.Inspection == 0">
            <template v-slot:activator="{ on }">
              <v-btn
                v-if="item.Inspection != 0"
                v-on="on"
                small
                text
                @click="showOtherPipes(item, 'Inspection')"
                >{{ item.Inspection }}</v-btn
              >
              <v-btn v-else v-on="on" small text>{{
                0
              }}</v-btn>
            </template>
            <span v-if="item.Inspection != 0">Show Pipes</span>
          </v-tooltip>
        </template>

        <template v-slot:item.Hardbanding="{ item }">
          <v-tooltip left :disabled="item.Hardbanding == 0">
            <template v-slot:activator="{ on }">
              <v-btn
                v-if="item.Hardbanding != 0"
                v-on="on"
                small
                text
                @click="showOtherPipes(item, 'Hardbanding')"
                >{{ item.Hardbanding }}</v-btn
              >
              <v-btn v-else v-on="on" small text>{{
                0
              }}</v-btn>
            </template>
            <span>Show Pipes</span>
          </v-tooltip>
        </template>

        <template v-slot:item.Booked="{ item }">
          <v-tooltip left :disabled="item.Booked == 0">
            <template v-slot:activator="{ on }">
              <v-btn
                v-if="item.Booked != 0"
                v-on="on"
                small
                text
                @click="showOtherPipes(item, 'Booked')"
                >{{ item.Booked }}</v-btn
              >
              <v-btn v-else v-on="on" small text>{{
                0
              }}</v-btn>
            </template>
            <span v-if="item.Booked != 0">Show Pipes</span>
          </v-tooltip>
        </template>

        <template v-slot:item.On_Hold="{ item }">
          <v-tooltip left :disabled="item.On_Hold == 0">
            <template v-slot:activator="{ on }">
              <v-btn
                v-if="item.On_Hold != 0"
                v-on="on"
                small
                text
                @click="showOtherPipes(item, 'On_Hold')"
                >{{ item.On_Hold }}</v-btn
              >
              <v-btn v-else v-on="on" small text>{{
                0
              }}</v-btn>
            </template>
            <span v-if="item.On_Hold != 0">Show Pipes</span>
          </v-tooltip>
        </template>

        <template v-slot:item.Wepco="{ item }">
          <v-tooltip left :disabled="item.Wepco == 0">
            <template v-slot:activator="{ on }">
              <v-btn
                v-if="item.Wepco != 0"
                v-on="on"
                small
                text
                @click="showOtherPipes(item, 'Wepco')"
                >{{ item.Wepco }}</v-btn
              >
              <v-btn v-else v-on="on" small text>{{
                0
              }}</v-btn>
            </template>
            <span v-if="item.Wepco != 0">Show Pipes</span>
          </v-tooltip>
        </template>

        <template v-slot:item.Stamas="{ item }">
          <v-tooltip left :disabled="item.Stamas == 0">
            <template v-slot:activator="{ on }">
              <v-btn
                v-if="item.Stamas != 0"
                v-on="on"
                small
                text
                @click="showOtherPipes(item, 'Stamas')"
                >{{ item.Stamas }}</v-btn
              >
              <v-btn v-else v-on="on" small text>{{
                0
              }}</v-btn>
            </template>
            <span v-if="item.Stamas != 0">Show Pipes</span>
          </v-tooltip>
        </template>
      </v-data-table>
    </v-card>
  </v-container>
</template>

<script>
import { mapGetters } from 'vuex'
import axios from 'axios'
import image from '../assets/picture.png'
import moment from 'moment'
export default {
  name: 'inventory',
  data () {
    return {
      location: '',
      pipe: {
        backgroundColor: 'pink'
      },
      header_min_height: 130,
      colormap: '',
      rackinfo: '',
      pipeload: false,
      image: image,
      allpipes: [],
      Itemnr: null,
      Serialnr: null,
      n: null,
      numbers: [],
      dialog: false,
      dialog2: false,
      dialog3: false,
      test: false,
      search: '',
      search2: '',
      headers2: [
        {
          text: 'Serial Number',
          align: 'start',
          sortable: true,
          value: 'Serial_Number'
        },
        { text: 'Rack Position', value: 'Rack_Position' },
        { text: 'Position', value: 'Position' },
        { text: 'Current Location', value: 'Current_Location' }
      ],
      headers3: [
        {
          text: 'Serial Number',
          align: 'start',
          sortable: true,
          value: 'Serial_Number'
        },
        { text: 'Date Inspected', value: 'Date_Inspected' }
      ],
      headers: [
        {
          text: 'Item Number',
          align: 'center',
          sortable: true,
          value: 'Item_No'
        },
        { text: 'Equipment', value: 'Equipment' },
        { text: 'Site', value: 'Site' },
        { text: 'Rig Ready', value: 'Rig_Ready' },
        { text: 'Inspection', value: 'Inspection' },
        { text: 'Booked', value: 'Booked' },
        { text: 'Backlog', value: 'Backlog' },
        { text: 'Wepco', value: 'Wepco' },
        { text: 'Stamas', value: 'Stamas' },
        { text: 'Hardbanding', value: 'Hardbanding' },
        { text: 'Scrap', value: 'Scrap' },
        { text: 'Limited Service', value: 'Limited_Service' },
        { text: 'On Hold', value: 'On_Hold' },
        { text: 'Other', value: 'Other' },
        { text: 'Total Onshore', value: 'Total_Yard' },
        { text: 'Certificates', sortable: false, value: 'action' }
      ],
      desserts: []
    }
  },
  mounted () {
    this.test = true
    axios
      .get('/getInventory', {
        params: { username: this.$store.getters.getUsername }
      })
      .then(response => {
        console.log(response)
        this.desserts = response.data
        this.test = false
      })
  },
  methods: {
    computeColor(pipe) {
      if(Object.keys(this.colormap).length !== 0) {
        return this.colormap[pipe].color;
      } else {
        return 'white'
      }
    },
    getPDF (link) {
      console.log(link.PDF)
      window.open(link.PDF, '_blank')
    },
    showRack (pipedata) {
      this.pipeload = true
      console.log(pipedata.Rack_Position)
      this.Serialnr = pipedata.Serial_Number
      axios
        .get('/getPipes', {
          params: { rackname: pipedata.Rack_Position }
        })
        .then(response => {
          this.pipeload = false
          console.log(response.data.rackinfo)
          this.n = response.data.rackinfo.Maxrowcount
          this.allpipes = response.data.pipes
          this.rackinfo = response.data.rackinfo
          this.colormap = response.data.colormap
          this.dialog2 = true
        })
    },
    clearList () {
      this.numbers = []
      this.dialog = false
      this.dialog3 = false
      this.Itemnr = null
    },
    clearRack () {
      this.dialog2 = false
      this.n = null
      this.allpipes = []
      this.rackinfo = ''
    },
    showPipes (item) {
      if (item.Rig_Ready > 0) {
        this.test = true
        axios
          .get('showPipelist', {
            params: { itemnr: item.Item_No }
          })
          .then(response => {
            console.log(response)
            this.numbers = response.data
            this.test = false
            this.dialog = true
            this.Itemnr = item.Item_No
          })
      }
    },
    getDateDiff: function (pipe) {
      var now = moment(new Date())
      var end = moment(pipe.Date_Inspected)
      var duration = moment.duration(now.diff(end))
      var days = duration.asDays()
      return days
    },
    showOtherPipes (item, location) {
      console.log(location)
      this.test = true
      axios
        .get('/showOtherlist', {
          params: { itemnr: item.Item_No, location: location }
        })
        .then(response => {
          console.log(response)
          this.numbers = response.data
          this.test = false
          this.dialog3 = true
          this.location = location
          this.Itemnr = item.Item_No
        })
    }
  },
  computed: {
    ...mapGetters(['getUsername','getAsset','getFleet']),
    divideRows () {
      const chunkarray = []
      const fullarray = this.allpipes
      let i
      let j
      let temparray
      const chunk = this.n
      // Change for several maxrowcounts
      for (i = 0, j = fullarray.length; i < j; i += chunk) {
        temparray = fullarray.slice(i, i + chunk)
        chunkarray.push(temparray)
      }
      return chunkarray.reverse()
    },
    filterItems() {
      if (this.getFleet === true) {
        return this.desserts;
      } else {
        return this.desserts.filter(item => {
          return item.Asset === this.getAsset;
        });
      }
    }
  }
}
</script>
<style>
.tooltippen {
  text-align: center;
}
.test {
  background-color: aqua;
}
table {
  margin: auto;
}
.tdclass {
  border: 1px solid black;
  padding: 1px;
}

.v-data-table-header th {
  white-space: nowrap;
}
</style>
