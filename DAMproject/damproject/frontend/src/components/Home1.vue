<template>
  <!-- Thumbnails 使用poptrox-->
  <!--            <section v-for="classi in imgList">-->
  <!--              <header class="_30jhRtnB" style="height: 44px">-->
  <!--                            <h2 class="_2uvC445S">{{classi.key}}</h2>-->
  <!--                            <a class="_6Xeq5Ikb _3rHyVhAS" @click="tocate(classi.key)">-->
  <!--                              <span class="_1_4B_gHA">更多</span>-->
  <!--                              <svg aria-label="Arrow right" class="_2YAsIJAi _3f8vV4uW" role="img" tabindex="-32768"-->
  <!--                                   viewBox="0 0 28.9 7.8" xmlns="http://www.w3.org/2000/svg">-->
  <!--                                <path d="M 25 3.2 H 0.7 c -0.4 0 -0.7 0.3 -0.7 0.7 c 0 0.4 0.3 0.7 0.7 0.7 H 25 c 0.4 0 0.7 -0.3 0.7 -0.7 c 0 -0.4 -0.3 -0.7 -0.7 -0.7 Z"/>-->
  <!--                                <path d="M 24.4 4.7 V 0.4 c 0 -0.4 0.3 -0.6 0.6 -0.3 l 1.2 1.1 c 0.3 0.3 0.9 0.8 1.2 1.1 l 1.2 1.1 c 0.3 0.3 0.3 0.8 0 1.1 l -1.2 1.1 c -0.3 0.3 -0.9 0.8 -1.2 1.1 l -1.2 0.9 c -0.3 0.3 -0.6 0.2 -0.6 -0.3 V 4.7 Z"/>-->
  <!--                              </svg>-->
  <!--                            </a>-->
  <!--                          </header>-->
  <!--              <ul class="ELHm5RGs">-->
  <!--                <li v-for="img in classi.value" class="_2-KcWAGg">-->
  <!--                  <section class="thumbnails" style="margin-left: 10%; margin-right: 10%">-->
  <!--                    <div class="v-waterfall-content" id="v-waterfall">-->
  <!--                      <div class="v-waterfall-item">-->
  <!--                        <div class="icons">&lt;!&ndash; 三个icon按钮 &ndash;&gt;-->
  <!--                                  <ul @mouseout="leaveul($event)" @mouseover="enterul($event)">-->
  <!--                                    <li><p @click="clickCollect($event)" class="icon style2 fa-star"-->
  <!--                                           v-bind:class="{ Collected:img.state }"><span class="label">Collect</span></p></li>-->
  <!--                                    <li><p @click="clickLike($event)" class="icon style2 fa-thumbs-up"-->
  <!--                                           v-bind:class="{ Likeded:img.state }"><span class="label">Like</span></p></li>-->
  <!--                                    <li><a class="icon style2 fa-info" data-poptrox="iframe,1200x800" href="index.html"><span-->
  <!--                                      class="label">ForMore</span></a></li>-->

  <!--                                  </ul>-->
  <!--                                </div>-->
  <!--                        <div class="labels">&lt;!&ndash; labels链接 &ndash;&gt;-->
  <!--                          <ul :style="{top:this.imgheight+ 20 +'px'}" @mouseout="leaveul_la($event)" @mouseover="enterul_la($event)" class="KSVul">-->
  <!--                            <a href="#" v-for="tag in img.tags">{{'#'+tag}}</a>-->
  <!--                          </ul>-->
  <!--                        </div>-->
  <!--                        <a>-->
  <!--                          <img :id="img.id" :src="img.img" @mouseenter="enterpic($event)" @mouseleave="leavepic($event)"-->
  <!--                               alt="" style="width: 100%; height: 100%; position: absolute; inset: 0px;">-->
  <!--                        </a>-->
  <!--                      </div>-->
  <!--                    </div>-->
  <!--                  </section>-->
  <!--                </li>-->
  <!--              </ul>-->
  <!--            </section>-->

  <section id="main" style="align-content: center;align-items: center">
    <header>
    </header>
    <section class="thumbnails" style="margin-left: 10%; margin-right: 10%">
      <div class="v-waterfall-content" id="v-waterfall1" style="padding-top: 50px;">
        <div>
          <section v-for="count in cate_num">
            <div class="Cat">
            <div>
              <h2 class="Titleeeee" @click="tocate(classname[count-1])">{{classname[count-1]}}</h2>
            </div>
            <div class="Line">
              <div v-for="img in imgList[count-1]"
                 class="v-waterfall-item"
                 :style="{top:90+'px',left:img.left+30+'px',width:250+'px',height:250+'px','padding-right':10+'px'}">
              <div class="icons"> <!-- 三个icon按钮 -->
                <ul @mouseout="leaveul($event)" @mouseover="enterul($event)"
                    :style="{top:imgheight-395+'px',right:3+'%'}">
                  <li><p @click="clickCollect($event)" class="icon style2 fa-star" v-bind:class="{ Collected:img.state }"><span class="label">Collect</span></p>
                  </li>
                  <li><p @click="clickLike($event)" class="icon style2 fa-thumbs-up" v-bind:class="{ Likeded:img.state }"><span class="label">Like</span></p>
                  </li>
                  <li><a class="icon style2 fa-info" data-poptrox="iframe,1200x800" href="index.html"><span class="label">ForMore</span></a>
                  </li>
                </ul>
              </div>
              <div class="labels"><!-- labels链接 -->
                <ul :style="{top:imgheight-185+'px'}" @mouseout="leaveul_la($event)" @mouseover="enterul_la($event)"
                    class="KSVul">
                  <a>{{img.tags}}</a>
                </ul>
              </div>
              <div class="Img-Iput">
                <div class="img_inputBox" @mouseenter="enterpic($event)" @mouseleave="leavepic($event)">
                  <img :id="img.id" :src="img.img" alt="" class="img-inputer">
                </div>
              </div>
            </div>
            </div>
          </div>
          </section>
        </div>


<!--        <div>-->
<!--          <div :style="{'padding-top': 340+'px'}">-->
<!--            <router-link to="/chrome" class="Titleeeee">食物</router-link>-->
<!--          </div>-->
<!--          <div v-for="img in ShowList"-->
<!--               class="v-waterfall-item"-->
<!--               :style="{top:520+'px',left:img.left+30+'px',width:250+'px',height:250+'px','padding-right':10+'px','z-index': 0}">-->
<!--            &lt;!&ndash;            <router-link to="/chrome" class="Titleeeee">食物</router-link>&ndash;&gt;-->
<!--            <div class="icons"> &lt;!&ndash; 三个icon按钮 &ndash;&gt;-->
<!--              <ul @mouseout="leaveul($event)" @mouseover="enterul($event)"-->
<!--                  :style="{top:imgheight-395+'px',right:3+'%'}">-->
<!--                <li><p @click="clickCollect($event)" class="icon style2 fa-star"><span class="label">Collect</span></p>-->
<!--                </li>-->
<!--                <li><p @click="clickLike($event)" class="icon style2 fa-thumbs-up"><span class="label">Like</span></p>-->
<!--                </li>-->
<!--                <li><a class="icon style2 fa-info" data-poptrox="iframe,1200x800" href="index.html"><span class="label">ForMore</span></a>-->
<!--                </li>-->
<!--              </ul>-->
<!--            </div>-->
<!--            <div class="labels">&lt;!&ndash; labels链接 &ndash;&gt;-->
<!--              <ul :style="{top:imgheight-185+'px'}" @mouseout="leaveul_la($event)" @mouseover="enterul_la($event)"-->
<!--                  class="KSVul">-->
<!--                <a href="#">#AAA</a>-->
<!--                <a href="#">#AAA</a>-->
<!--                <a href="#">#AAA</a>-->
<!--              </ul>-->
<!--            </div>-->
<!--            <div class="Img-Iput">-->
<!--              <div class="img_inputBox" @mouseenter="enterpic($event)" @mouseleave="leavepic($event)">-->
<!--                <img :src="img.src" alt="" class="img-inputer">-->
<!--              </div>-->
<!--            </div>-->
<!--          </div>-->
<!--        </div>-->
      </div>

    </section>
  </section>
</template>

<script>
    export default {
        name: "Home",
        data() {
            return {
                imgList: [],
                cate_num: 5,
                each_num: 4,
                my_id: '',
                imgheight: 400,
                classname: [],
            }
        },
        created() {
            this.my_id = this.$store.state.user_id;

        },
        mounted() {
            this.getcate();
        },

        methods: {
            tocate(k){
              this.$router.replace({path:'/category/' + k});
            },
            enterpic(e) {
                //icon
                e.currentTarget.parentElement.previousElementSibling.previousElementSibling.firstElementChild.className = "IconOver";
                var label_number = e.currentTarget.parentElement.previousElementSibling.firstElementChild.childElementCount;
                var children = e.currentTarget.parentElement.previousElementSibling.firstElementChild.children;
                for (var i = 0; i < label_number; i++) {
                    children[i].className = "LabelsOver";
                }
            },
            leavepic(e) {
                //icon
                e.currentTarget.parentElement.previousElementSibling.previousElementSibling.firstElementChild.className = "IconOut";
                var label_number = e.currentTarget.parentElement.previousElementSibling.firstElementChild.childElementCount;
                var children = e.currentTarget.parentElement.previousElementSibling.firstElementChild.children;
                for (var i = 0; i < label_number; i++) {
                    children[i].className = "LabelsOut";
                }
            },
            enterul(e) {
                e.currentTarget.className = "IconOver";
                //label
                var label_number = e.currentTarget.parentElement.nextElementSibling.firstElementChild.childElementCount;
                var children = e.currentTarget.parentElement.nextElementSibling.firstElementChild.children;
                for (var i = 0; i < label_number; i++) {
                    children[i].className = "LabelsOver";
                }
            },
            leaveul(e) {
                e.currentTarget.className = "IconOut";
                //label
                var label_number = e.currentTarget.parentElement.nextElementSibling.firstElementChild.childElementCount;
                var children = e.currentTarget.parentElement.nextElementSibling.firstElementChild.children;
                for (var i = 0; i < label_number; i++) {
                    children[i].className = "LabelsOut";
                }
            },
            enterul_la(e) {
                var label_number = e.currentTarget.childElementCount;
                var children = e.currentTarget.children;
                for (var i = 0; i < label_number; i++) {
                    children[i].className = "LabelsOver";
                }
                e.currentTarget.parentElement.previousElementSibling.firstElementChild.className = "IconOver";
            },
            leaveul_la(e) {
                var label_number = e.currentTarget.childElementCount;
                var children = e.currentTarget.children;
                for (var i = 0; i < label_number; i++) {
                    children[i].className = "LabelsOut";
                }
                e.currentTarget.parentElement.previousElementSibling.firstElementChild.className = "IconOut";
            },
            getcate() {
                this.$api.post('/get_images', {number: this.each_num, email: this.my_id}).then(response => {
                    if(response.data != 'Not received'){
                        console.log(response.data)
                        this.cate_num = response.data.length;
                        for (let i = 0; i < this.cate_num; i++) {
                            this.classname.push(Object.keys(response.data[i]));
                            let list = response.data[i][this.classname[i]];
                            // this.imgList.left = i * 300;
                            // list.left = i * 300;
                            this.imgList.push(list)
                            console.log(list);
                            // for (let j = 0; j < 4; j++) {
                            //     list[j].left = 300 * i;
                            //     console.log(list[j]);
                            // }
                        console.log('classname : '+(this.classname[i]))
                        console.log('imgs' +this.imgList[i])
                        }
                    }
                        // // for (let key in keys) {
                        //     console.log(keys)
                        //     this.imgList.images = response.data[0][keys]
                        // }
                      // console.log(response.data[0], this.imgList);


                      // this.imgList = response.data;
                      // console.log('imglist'+this.imgList)
                      // console.log('num'+this.cate_num)

                }), (response) => {
                    console.log("error");
                    this.$message.error('获取图片失败');
                }
                this.preloading();
            },
            preloading() {
                for (let i = 0; i < this.cate_num; i++) {
                    for (let j = 0; j < this.each_num; j++) {

                    }
                }
            },
            //点赞
            thumb_click(e) {
                let flag = true;
                if (e.currentTarget.className === "icon style2 fa-thumbs-up") {
                    e.currentTarget.className = "icon style2 fa-thumbs-up Liked";
                } else {
                    e.currentTarget.className = "icon style2 fa-thumbs-up";
                    flag = false;
                }
                this.$api.post('/like_image ', {
                    id: e.target.parentElement.parentElement.parentElement.lastElementChild.firstElementChild.getAttributeNode('id'),
                    email: this.my_id, state: flag
                }).then(response => {
                    //console.log(response.data);
                    if (response.data === 'SUCCESS') {
                        this.$message.success('成功');
                    }
                }), (response) => {
                    //console.log("error");
                    this.$message.error('失败');
                }
            },
            //收藏
            fav_click(e) {
                let flag = true;
                if (e.currentTarget.className === "icon style2 fa-star") {
                    e.currentTarget.className = "icon style2 fa-star Collected";
                } else {
                    e.currentTarget.className = "icon style2 fa-star";
                    flag = false;
                }
                this.$api.post('/like_image ', {
                    id: e.target.parentElement.parentElement.parentElement.lastElementChild.firstElementChild.getAttributeNode('id'),
                    email: this.my_id, state: flag
                }).then(response => {
                    //console.log(response.data);
                    if (response.data === 'SUCCESS') {
                        //改变按钮状态
                        this.$message.success('成功');
                    }
                }), (response) => {
                    //console.log("error");
                    this.$message.error('失败');
                }
            },
        }
    }


</script>

<style scoped>
  .Liked {
    color: rgb(238, 106, 132);
  }

  .Collected {
    color: rgb(238, 203, 106);
  }

  .LabelsOver {
    visibility: visible;
    opacity: 1;
    -webkit-transform: translateY(100%);
    transform: translate(0, 25%) !important;
    transition: all 0.3s ease-in-out;
  }

  .LabelsOut {
    visibility: hidden;
    opacity: 0;
    -moz-transform: translateY(100%);
    -webkit-transform: translateY(100%);
    -ms-transform: translateY(100%);
    transform: translateY(20px) !important;
    -webkit-transition: all 1s ease-in-out;
    transition: all 0.3s ease-in-out;
  }
  .IconOver {
    visibility: visible;
    opacity: 1;
    -webkit-transform: translate(0, -100%);
    transform: translate(0, 25%) !important;
    transition: all 0.3s ease-in-out;
  }
  .IconOut {
    visibility: hidden;
    opacity: 0;
    -moz-transform: translateY(-100%);
    -webkit-transform: translateY(-100%);
    -ms-transform: translateY(-100%);
    transform: translateY(-10%) !important;
    -webkit-transition: all 1s ease-in-out;
    transition: all 0.3s ease-in-out
  }
  .v-waterfall-content {
    padding-top: 20px;
  }
  .Titleeeee {
    text-decoration: none;
    /*font-family: Serif, serif;*/
    font-family: "Source Sans Pro", sans-serif;
    font-size: 35px;
    font-weight: 300;
    margin: 0;
    z-index: 100;
  }

  .Img-Iput {
    top: 0;
    /*margin-top: 60px;*/
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 250px;
    height: 250px;
    border-radius: 5px;
    background-color: rgba(26, 25, 29, 0.84);
  }

  .img_inputBox {
    position: relative;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    width: 250px;
    height: 250px;
    border-radius: 5px;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .img-inputer {
    position: relative;
    top: 0;
    z-index: 0;
    width: auto;
    height: 100%;
  }

  .thumbnails .v-waterfall-content {
    width: 100%;
    height: 100%;
    position: absolute;
  }

  .thumbnails .v-waterfall-content .v-waterfall-item {
    float: left;
    position: absolute;
  }

</style>
