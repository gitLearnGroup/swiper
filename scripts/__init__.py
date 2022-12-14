import os
import sys
import django

swiper_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
packed_path = sys.path
packed_path.insert(0, swiper_path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swiper.settings')
django.setup()

from user.models import User
from vip.models import Vip, Permission, VipPermRelative

first_name = [
   '赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
   '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章', '云',
   '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳', '酆', '鲍',
   '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常', '乐', '于', '时',
   '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹', '姚', '邵', '湛', '汪',
   '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞', '熊', '纪', '舒', '屈', '项',
   '董', '梁', '杜', '阮', '蓝', '闵', '席', '季', '麻', '强', '贾', '路', '娄', '危', '江', '童', '颜', '郭', '梅', '盛',
   '刁', '钟', '徐', '邱', '骆', '高', '夏', '蔡', '田', '樊', '胡', '凌', '霍', '虞', '万', '支', '柯', '昝', '管', '卢',
   '经', '房', '裘', '缪', '干', '解', '应', '宗', '丁', '宣', '贲', '邓', '郁', '单', '杭', '洪', '包', '诸', '左', '石',
   '吉', '钮', '龚', '程', '嵇', '邢', '滑', '裴', '陆', '荣', '翁', '荀', '羊', '於', '惠', '甄', '麴', '家', '封', '芮',
   '储', '靳', '汲', '邴', '糜', '松', '井', '段', '富', '巫', '乌', '焦', '巴', '弓', '牧', '隗', '山', '谷', '车', '侯',
   '蓬', '全', '郗', '班', '仰', '秋', '仲', '伊', '宫', '宁', '仇', '栾', '暴', '甘', '钭', '厉', '戎', '祖', '武', '符',
   '景', '詹', '束', '龙', '叶', '幸', '司', '韶', '郜', '黎', '蓟', '薄', '印', '宿', '白', '怀', '蒲', '邰', '从', '鄂',
   '咸', '籍', '赖', '卓', '蔺', '屠', '蒙', '池', '乔', '阴', '欎', '胥', '能', '苍', '双', '闻', '莘', '党', '翟', '谭',
   '劳', '逄', '姬', '申', '扶', '堵', '冉', '宰', '郦', '雍', '舄', '璩', '桑', '桂', '濮', '牛', '寿', '通', '边', '扈',
   '冀', '郏', '浦', '尚', '农', '温', '别', '庄', '晏', '柴', '瞿', '阎', '充', '慕', '连', '茹', '习', '宦', '艾', '鱼',
   '向', '古', '易', '慎', '戈', '廖', '庾', '终', '暨', '居', '衡', '步', '都', '耿', '满', '弘', '匡', '国', '文', '寇',
   '禄', '阙', '东', '殴', '殳', '沃', '利', '蔚', '越', '夔', '隆', '师', '巩', '厍', '聂', '晁', '勾', '敖', '融', '冷',
   '辛', '阚', '那', '简', '饶', '空', '曾', '毋', '沙', '乜', '养', '鞠', '须', '丰', '巢', '关', '蒯', '相', '查', '後',
   '红', '游', '竺', '权', '逯', '盖', '益', '桓', '公', '万俟', '司马', '上官', '欧阳', '夏侯', '诸葛', '闻人', '东方', '赫连', '皇甫', '尉迟',
   '澹台', '公冶', '宗政', '濮阳', '淳于', '单于', '太叔', '申屠', '公孙', '仲孙', '轩辕', '令狐', '钟离', '宇文', '长孙', '慕容', '鲜于', '闾丘', '司徒', '司空',
   '司寇', '仉', '督', '子车', '颛孙', '端木', '巫马', '公西', '漆雕', '乐正', '壤驷', '公良', '拓跋', '夹谷', '宰父', '谷梁', '晋', '楚', '闫', '法',
   '鄢', '涂', '钦', '段干', '百里', '东郭', '南门', '呼延', '归', '海', '羊舌', '微生', '岳', '帅', '缑', '亢', '况', '后', '有', '琴',
   '左丘', '东门', '西门', '商', '牟', '佘', '佴', '伯', '赏', '南宫', '墨', '哈', '谯', '笪', '年', '爱', '阳', '佟', '第五', '言'
]

sex = ['男', '女']

last_name = {
    '男': [
       '博超', '俊源', '高风', '鸿达', '杰恩', '雨韵', '荣景', '鼎茂', '弘岩', '智辰', '风震', '宇悠', '煜城', '昌月', '浩楠', '辉弘', '崇雨', '玮楷', '云悠', '辉翰',
       '健翎', '彬浪', '晋泰', '松德', '泽恩', '鼎国', '涛源', '昌尘', '泽国', '荣恩', '乾君', '圣德', '博鹤', '风沙', '圣豪', '旭翔', '苑杰', '韵沙', '玮轩', '涛德',
       '柏轩', '鼎润', '棋杰', '城天', '鸿文', '春生', '宇雷', '杉余', '玮瀚', '柏翔', '涛锦', '旭乔', '浩彤', '浩润', '新诚', '辉彤', '涛信', '博运', '晋拓', '畅德',
       '文锋', '俊洪', '晓柯', '展信', '智云', '文翔', '鸿轩', '鼎新', '展博', '文方', '玮靖', '玮彤', '松阳', '晓诚', '泽柳', '博玮', '展豪', '彤博', '智睿', '文啸',
       '尧畅', '文勇', '志伟', '玮若', '苑宇', '韵文', '桦佑', '雪博', '玮龙', '昌影', '浩彦', '辉宇', '翰拓', '文博', '昌易', '涛崇', '涛天', '彤逸', '阔畅', '文清',
       '昌蝶', '柏瀚', '文泰', '展邦', '翰楠', '言明', '致浩', '劲玮', '羽春', '韵来', '棋韵', '远瑞', '浩然', '若兴', '彬瀚', '晓然', '弘玉', '远林', '江德', '雨国',
       '文树', '志明', '博江', '德元', '曲鸣', '棋渊', '德星', '彬睿', '杰霖', '文奇', '秀棋', '晋文', '秀宇', '杰诚', '博昌', '彬辉', '荣畅', '弘振', '紫然', '博振',
       '楠天', '晋凯', '文翰', '瀚松', '弘伦', '江南', '俊新', '秀轩', '泽伟', '哲楠', '如鸿', '昊哲', '泽辉', '明泽', '文易', '浩璋', '万里', '鼎拓', '文源', '瀚宇',
       '浩云', '浩桦', '博欢', '智恒', '智伟', '健国', '风欧', '文岩', '博文', '彬月', '文江', '棋泽', '文元', '贵博', '星磊', '世承', '涛图', '亦君', '韵润', '翰晖'
    ],
    '女': [
       '紫莺', '映花', '冰云', '羽珊', '璐瑶', '寻真', '丹丹', '秋月', '玉娟', '雪春', '雨莉', '紫奇', '雨彤', '梨颖', '痴珊', '欣怡', '紫芝', '雁玉', '佳诺', '云柏',
       '含蕾', '可悦', '雨萱', '盼海', '璐萱', '焕语', '佳欣', '馥婉', '烟媛', '蓉蓉', '佳璐', '文涓', '欣慧', '雨欣', '冰丹', '夜云', '彩樱', '佳诗', '怀柔', '锦悦',
       '馨彤', '仙琳', '香波', '若雪', '云雪', '心韵', '雨婷', '盈璐', '翠婉', '翠萱', '香怡', '艺涵', '芷蕾', '诗雨', '江甜', '雯昕', '丝雯', '雅倩', '雪慧', '雅欣',
       '倚蓉', '晴翠', '晴阳', '依灵', '凤荷', '昕怡', '乐璇', '凤乐', '欢旋', '芊缘', '昕莹', '新蕊', '偌孜', '仪婷', '漫旋', '雨芯', '逸敏', '云昕', '妍欣', '欣新',
       '梨虞', '云燕', '丹玉', '珊芹', '甜亦', '雅新', '竹君', '玲玉', '尔珍', '琪芸', '文丽', '雅霜', '紫璇', '觅波', '玫桑', '妙佳', '梦沁', '嘉玲', '凝芙', '缘绿',
       '雅柏', '平绿', '雅淑', '柳清', '盈盈', '茹桃', '竹凤', '若汐', '茹雅', '琴岚', '梦遥', '迎波', '亚蕾', '欣月', '含卉', '可嘉', '思甜', '柏桃', '楚卿', '涵柳',
       '诗霜', '黛柔', '绮玉', '桐熙', '晴霎', '秀思', '丹燕', '曼香', '谷丝', '含清', '云青', '露露', '璇沛', '雅兰', '万婷', '依枝', '雅绿', '菲玉', '雨雯', '芸菱',
       '卉雪', '雪怡', '露莹', '海葵', '冰颖', '一荃', '绿芸', '问旋', '缘柏', '沛菡', '缘雯', '安南', '冰林', '忆彤', '沛纹', '晓雨', '亦梦', '红霞', '紫露', '芊芸',
       '菲舞', '雅萱', '歆素', '月荷', '雅妮', '梦岚', '采佳', '蕾云', '若壁', '雪巧', '雨绮', '痴梦', '欣瑜', '雨萌', '佳仪', '晓苹', '思贝', '珊漫', '馨语', '雅轩'
    ]
}


def make_name():
    from random import choice
    current_sex = choice(sex)
    name = choice(first_name) + choice(last_name[current_sex])
    return name, current_sex


def make_robot():
    from random import randrange, choice
    for i in range(1000):
        try:
            nickname, cur_sex = make_name()
            User.objects.create(
                nickname=nickname,
                phonenum=randrange(20000000000, 29999999999),
                sex=cur_sex,
                location=choice(['北京', '上海', '武汉', '郑州']),
                birth_year=randrange(1980, 2000),
                birth_month=randrange(1, 13),
                birth_day=randrange(1, 28)
            )
        except:
            pass


def make_vip():
    for i in range(4):
        Vip.objects.create(
            name=f"vip_{i}",
            level=i,
            price=5*i
        )
    print('vip数据制造成功')


def make_permission():
    for name in ['vip_flag', 'super_like', 'rewind', 'any_location', 'not_limit_like']:
        Permission.objects.create(name=name)
    print('permission数据制造成功')


def make_relative():
    vip_1 = Vip.objects.get(level=1)
    vip_2 = Vip.objects.get(level=2)
    vip_3 = Vip.objects.get(level=3)

    vip_flag = Permission.objects.get(name='vip_flag')
    super_like = Permission.objects.get(name='super_like')
    rewind = Permission.objects.get(name='rewind')
    any_location = Permission.objects.get(name='any_location')
    not_limit_like = Permission.objects.get(name='not_limit_like')

    VipPermRelative.objects.create(vip_id=vip_1.id, perm_id=vip_flag.id)
    VipPermRelative.objects.create(vip_id=vip_1.id, perm_id=super_like.id)

    VipPermRelative.objects.create(vip_id=vip_2.id, perm_id=vip_flag.id)
    VipPermRelative.objects.create(vip_id=vip_2.id, perm_id=rewind.id)
    
    VipPermRelative.objects.create(vip_id=vip_3.id, perm_id=vip_flag.id)
    VipPermRelative.objects.create(vip_id=vip_3.id, perm_id=super_like.id)
    VipPermRelative.objects.create(vip_id=vip_3.id, perm_id=rewind.id)
    VipPermRelative.objects.create(vip_id=vip_3.id, perm_id=any_location.id)
    VipPermRelative.objects.create(vip_id=vip_3.id, perm_id=not_limit_like.id)
    print('relative数据制造成功')


if __name__ == '__main__':
    # make_robot()
    # make_vip()
    # make_permission()
    make_relative()

