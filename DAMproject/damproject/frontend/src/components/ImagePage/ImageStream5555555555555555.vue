<template>
  <div class="ImageStream">
    <section id="main" style="align-content: center;align-items: center">
					<!-- Thumbnails 使用poptrox-->
    <section class="thumbnails" style="margin-left: 10%; margin-right: 10%">
    <div class="v-waterfall-content" id="v-waterfall">
      <div v-for="img in waterfallList"
           class="v-waterfall-item"
           :style="{top:img.top+'px',left:img.left+'px',width:waterfallImgWidth+'px',height:img.height+20+'px'}">
          <div class="icons"><!-- 三个icon按钮 -->
              <ul @mouseover="enterul($event)" @mouseout="leaveul($event)">
                <li><p class="icon style2 fa-star" @click="fav_click($event)" v-bind:class="{ Collected:img.state }" ><span class="label">Collect</span></p></li>
                <li><p class="icon style2 fa-thumbs-up" @click="thumb_click($event)" v-bind:class="{ Likeded:isLike }"><span class="label">Like</span></p></li>
                <li><a href="index.html" class="icon style2 fa-info" data-poptrox="iframe,1200x800"><span class="label">ForMore</span></a></li>
              </ul>
          </div>
        <div class="labels">
          <ul @mouseover="enterul_la($event)" @mouseout="leaveul_la($event)" class="KSVul" :style="{top:img.height+'px'}"><!-- labels链接 -->
            <a class="" href="#">{{'#'+img.classification}}</a>
            <a  class="" href="#">{{img.tags}}</a>
          </ul>
        </div>
        <a>
          <img @mouseenter="enterpic($event)" @mouseleave="leavepic($event)" :id="img.id" :src="img.img" alt="">
        </a>
      </div>
    </div>
  </section>

    </section>
  </div>
</template>

<script>
  import mouse_hover from "../../../static/js/userpage.js";
    export default {
        name: "ImageStream",
        data(){
            return {
                key: 'all',//检索关键词
                my_id: '',
                type: 0,//0是全局搜索，1是收藏，2是上传，3是类别
                isCollect:false,
                isLike: false,

                imgList: [],//从后端获取到的图片包括图片的url\id\tags\like\favorite\thumb
                count: 0,//已经从后端获取的图片数量
                last: 0,//List中未被加载的图片数量
                each_time: 10,//每次加载的图片数量
                imgArr:[],//当次要加载的图片
                waterfallList:[],//已经加载的照片

                waterfallImgWidth:350,
                waterfallImgCol:3,
                waterfallImgRight:10,
                waterfallImgBottom:10,
                waterfallDeviationHeight:[],
                threshold: 20,
            }
        },
        created() {
            console.log("created")
            this.my_id = this.$store.state.user_id;
            this.key = this.$route.params.key;
            this.log_img();
        },
        mounted(){
            console.log("mounted")
        },
        methods:{
            log_img(){
                //用户页
                if (this.$route.params.id !== undefined){
                    console.log("xxx")
                    if(this.$route.params.type === 'channel') this.type = 2;
                    else if(this.$route.params.type === 'favorite') this.type = 1;
                    console.log(this.type,this.key)
                    this.get_user(this.$route.params.id,this.type,this.key);
                }
                //搜索、类别页
                else {
                    console.log('search11111111')
                    if(this.$route.params.type === 'search') this.type = 0;
                    else if(this.$route.params.type === 'category') this.type = 3;
                    console.log(this.type,this.key)
                    this.get_img(this.type,this.key);
                }
            },

            scrollEvent(){
                let pageHeight = $('body').height(),
                    scrollTop = $(window).scrollTop(),
                    winHeight = $(window).height(),
                    thresold = pageHeight - scrollTop - winHeight;
                if (thresold > -100 && thresold <= 20) {
                }
                if (document.body.scrollTop+ document.body.clientHeight>= document.body.scrollHeight-this.threshold) {
                    console.log('end');
                    if(this.last){
                        this.load_more();
                        this.imgPreloading();
                    }

                }
            },
            //一次加载10张图片
            load_more(){
                // console.log('moremoremore')
                this.imgArr = []

                console.log('List\n'+this.imgList)
                for (let i = 0; i < this.each_time; i++){
                    if(this.last === 0) {
                        break;
                    }
                    console.log("is"+this.last)
                    this.last--;
                    this.imgArr.push(this.imgList[this.last]);
                }
                console.log('Arr\n'+this.imgArr[0])
            },
            enterpic(e){
                //icon
                e.currentTarget.parentElement.previousElementSibling.previousElementSibling.firstElementChild.className = "IconOver";
                var label_number = e.currentTarget.parentElement.previousElementSibling.firstElementChild.childElementCount;
                var children = e.currentTarget.parentElement.previousElementSibling.firstElementChild.children;
                for(var i=0;i<label_number;i++){
                    children[i].className = "LabelsOver";
                }
            },
            leavepic(e){
                //icon
                e.currentTarget.parentElement.previousElementSibling.previousElementSibling.firstElementChild.className = "IconOut";
                var label_number = e.currentTarget.parentElement.previousElementSibling.firstElementChild.childElementCount;
                var children = e.currentTarget.parentElement.previousElementSibling.firstElementChild.children;
                for(var i=0;i<label_number;i++){
                    children[i].className = "LabelsOut";
                }
            },
            enterul(e){
                e.currentTarget.className = "IconOver";
                //label
                var label_number = e.currentTarget.parentElement.nextElementSibling.firstElementChild.childElementCount;
                var children = e.currentTarget.parentElement.nextElementSibling.firstElementChild.children;
                for(var i=0;i<label_number;i++){
                    children[i].className = "LabelsOver";
                }
            },
            leaveul(e){
                e.currentTarget.className = "IconOut";
                //label
                var label_number = e.currentTarget.parentElement.nextElementSibling.firstElementChild.childElementCount;
                var children = e.currentTarget.parentElement.nextElementSibling.firstElementChild.children;
                for(var i=0;i<label_number;i++){
                    children[i].className = "LabelsOut";
                }
            },
            enterul_la(e){
                var label_number = e.currentTarget.childElementCount;
                var children = e.currentTarget.children;
                for(var i=0;i<label_number;i++){
                    children[i].className = "LabelsOver";
                }
                e.currentTarget.parentElement.previousElementSibling.firstElementChild.className = "IconOver";
            },
            leaveul_la(e){
                var label_number = e.currentTarget.childElementCount;
                var children = e.currentTarget.children;
                for(var i=0;i<label_number;i++){
                    children[i].className = "LabelsOut";
                }
                e.currentTarget.parentElement.previousElementSibling.firstElementChild.className = "IconOut";
            },

            //搜索结果
            get_img(t,k){
                this.$api.post('/get_user_image',{key:k,email:this.my_id,email_user:this.my_id,type:t}).then(response=>{
                    // console.log(response.data)
                    if(response.data != 'Not received'){
                        // console.log('lllldata:  '+response.data);
                        this.imgList = response.data;
                        console.log(this.imgList);
                        this.count += this.imgList.length;
                        this.last += response.data.length;
                        this.load_more();
                        this.calculationWidth();
                    }
                }),(response)=>{
                    //console.log("error");
                    this.$message('图片获取失败');
                }
            },
            //主页和收藏
            get_user(id,t,k){
                this.$api.post('/get_user_image',{key:k,email:id,type:t,email_user:this.my_id}).then(response =>{
                    // console.log(response.data);
                    if(response.data !== 'Not received'){
                        // console.log('lllldata:  '+response.data);
                        this.imgList = response.data;
                        this.count += this.imgList.length;
                        this.last += response.data.length;
                        this.load_more();
                        this.calculationWidth();
                    }

                }),(response)=>{
                    //console.log("error");
                    this.$message('图片获取失败');
                }
            },
            //计算每个图片的宽度或者是列数
            calculationWidth(){
                let domWidth = document.getElementById("v-waterfall").offsetWidth;
                if (!this.waterfallImgWidth && this.waterfallImgCol){
                    this.waterfallImgWidth = (domWidth-this.waterfallImgRight*this.waterfallImgCol)/this.waterfallImgCol;
                }else if(this.waterfallImgWidth && !this.waterfallImgCol){
                    this.waterfallImgCol = Math.floor(domWidth/(this.waterfallImgWidth+this.waterfallImgRight))
                }
                //初始化偏移高度数组
                this.waterfallDeviationHeight = new Array(this.waterfallImgCol);
                for (let i = 0;i < this.waterfallDeviationHeight.length;i++){
                    this.waterfallDeviationHeight[i] = 0;
                }
                this.preloading();
            },
            //按图片流格式预处理获得图片位置
            preloading(){
                for (let i = 0; i < this.imgArr.length; i++) {
                    let aImg = new Image();
                    aImg.src = this.imgArr[i].img;
                    aImg.onload = aImg.onerror = (e)=>{
                        let imgData = {};
                        imgData = this.imgArr[i];
                        imgData.height = this.waterfallImgWi1dth/aImg.width*aImg.height;
                        this.waterfallList.push(imgData);
                        this.rankImg(imgData);
                    }
                }
            },
            //瀑布流布局
            rankImg(imgData){
                let {waterfallImgWidth,waterfallImgRight,waterfallImgBottom,waterfallDeviationHeight,waterfallImgCol} = this;
                //for (let i = 0;i < this.waterfallList.length;i++){
                let minIndex = this.filterMin();
                imgData.top = waterfallDeviationHeight[minIndex];
                imgData.left = minIndex*(waterfallImgRight+waterfallImgWidth);
                waterfallDeviationHeight[minIndex] += imgData.height + waterfallImgBottom;
                //}
            },
            /**
             * 找到最短的列并返回下标
             * @returns {number} 下标
             */
            filterMin(){
                const min = Math.min.apply(null, this.waterfallDeviationHeight);
                return this.waterfallDeviationHeight.indexOf(min);
            },

            //点赞
            thumb_click(e){
                // let flag = true;
                if(e.currentTarget.className === "icon style2 fa-thumbs-up"){
                    e.currentTarget.className = "icon style2 fa-thumbs-up Liked";
                } else{
                    e.currentTarget.className = "icon style2 fa-thumbs-up";
                    // flag = false;
                }
                // this.$api.post('/like_image ',{id:e.target.parentElement.parentElement.parentElement.parentElement.lastElementChild.firstElementChild.getAttribute('id'),
                //     email:this.my_id,state: flag}).then(response =>{
                //         // console.log(e.target.parentElement.parentElement.parentElement.parentElement.lastElementChild.firstElementChild.getAttribute('id'),this.my_id,flag)
                //     //console.log(response.data);
                //     if(response.data === 'SUCCESS'){
                //         this.$message.success('成功');
                //     }
                // }),(response)=>{
                //     //console.log("error");
                //     this.$message.error('失败');
                // }
            },
            //收藏
            fav_click(e){
                let flag = true;
                if(e.currentTarget.className === "icon style2 fa-star"){
                    e.currentTarget.className = "icon style2 fa-star Collected";
                } else{
                    e.currentTarget.className = "icon style2 fa-star";
                    flag = false;
                }
                this.$api.post('/like_image ',{id:e.target.parentElement.parentElement.parentElement.lastElementChild.firstElementChild.getAttributeNode('id'),
                    email:this.my_id,state: flag}).then(response =>{
                    //console.log(response.data);
                    if(response.data === 'SUCCESS'){
                        //改变按钮状态
                        this.$message.success('成功');
                    }
                }),(response)=>{
                    //console.log("error");
                    this.$message.error('失败');
                }
            },
        }
    }
</script>

<style scoped>
  .Liked{
    color: rgb(238,106,132);
  }
  .Collected{
    color: rgb(238,203,106);
  }
  .LabelsOver{
    visibility: visible;
    opacity: 1;
    -webkit-transform: translateY(100%);
    transform: translate(0, 25%);
    transition: all 0.3s ease-in-out;
  }
  .LabelsOut {
    visibility: hidden;
    opacity: 0;
    -moz-transform: translateY(100%);
    -webkit-transform: translateY(100%);
    -ms-transform: translateY(100%);
    transform: translateY(20px);
    -webkit-transition: all 1s ease-in-out;
    transition: all 0.3s ease-in-out;
  }

  .IconOver {
    visibility: visible;
    opacity: 1;
    -webkit-transform: translate(0, -100%);
    transform: translate(0, 25%);
    transition: all 0.3s ease-in-out;
  }
  .IconOut {
    visibility: hidden;
    opacity: 0;
    -moz-transform: translateY(-100%);
    -webkit-transform: translateY(-100%);
    -ms-transform: translateY(-100%);
    transform: translateY(-10%);
    -webkit-transition: all 1s ease-in-out;
    transition: all 0.3s ease-in-out
  }
/* 可以设置不同的进入和离开动画 */
    /* 设置持续时间和动画函数 */
    .slide_fade-enter-active {
      transition: all .4s ease;
    }
    .slide_fade-leave-active {
      transition: all .4s cubic-bezier(1.0, 0.5, 0.8, 1.0);
    }
    .slide_fade-enter, .slide_fade-leave-to
   {
      transform: translateY(-10px);
      opacity: 0;
    }

.thumbnails .v-waterfall-content{
    width: 100%;
    height: 100%;
    position: absolute;
}
.thumbnails .v-waterfall-content .v-waterfall-item{
    float: left;
    position: absolute;
}
.v-waterfall-item img{
    width: 100%;
    height: auto;
}
</style>
