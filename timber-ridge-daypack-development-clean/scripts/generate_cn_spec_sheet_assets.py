from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / 'assets'
FONT = '/System/Library/Fonts/Hiragino Sans GB.ttc'

PAGES = [
    {
        'src': 'TimberRidgeDaypack_Spec_Viewer_p1.jpg',
        'dst': 'TimberRidgeDaypack_Spec_Viewer_p1_zh.jpg',
        'boxes': [
            {'box': (555, 4, 798, 34), 'text': 'TIMBER RIDGE 日用背包', 'size': 20, 'fill': 'sample', 'color': 'white'},
            {'box': (31, 126, 221, 150), 'text': '• 210D 小格纹防撕裂尼龙', 'size': 17},
            {'box': (33, 289, 228, 334), 'text': '• 织带缝入接缝中', 'size': 17},
            {'box': (34, 467, 165, 491), 'text': '• 压缩织带', 'size': 17},
            {'box': (529, 212, 642, 236), 'text': '丝印 LOGO', 'size': 17},
            {'box': (531, 287, 796, 350), 'text': '• 弹力网布包覆松紧包边后车缝\n• 不应看到松紧织带\n• 使用弹力线或人字缝线', 'size': 17, 'spacing': 4},
            {'box': (533, 390, 786, 415), 'text': '• 弹力网袋应紧贴包身', 'size': 17},
        ],
    },
    {
        'src': 'TimberRidgeDaypack_Spec_Viewer_p2.jpg',
        'dst': 'TimberRidgeDaypack_Spec_Viewer_p2_zh.jpg',
        'boxes': [
            {'box': (555, 4, 798, 34), 'text': 'TIMBER RIDGE 日用背包', 'size': 20, 'fill': 'sample', 'color': 'white'},
            {'box': (31, 167, 243, 200), 'text': '• 透气网布延伸包覆至前侧', 'size': 17},
            {'box': (33, 405, 242, 430), 'text': '• 所有五金均需同色配套', 'size': 17},
            {'box': (532, 211, 625, 235), 'text': '织唛标', 'size': 17},
            {'box': (529, 280, 736, 317), 'text': '• S 形肩带', 'size': 17},
            {'box': (529, 387, 763, 421), 'text': '• 整片菱形透气网背板', 'size': 17},
        ],
    },
    {
        'src': 'TimberRidgeDaypack_Spec_Viewer_p3.jpg',
        'dst': 'TimberRidgeDaypack_Spec_Viewer_p3_zh.jpg',
        'boxes': [
            {'box': (555, 4, 798, 34), 'text': 'TIMBER RIDGE 日用背包', 'size': 20, 'fill': 'sample', 'color': 'white'},
            {'box': (40, 172, 252, 230), 'text': '• 在笔电隔层后增加水袋隔层', 'size': 17},
            {'box': (40, 369, 205, 405), 'text': '• 加厚笔电隔层', 'size': 17},
            {'box': (529, 208, 628, 236), 'text': '织唛标', 'size': 17},
            {'box': (529, 385, 767, 447), 'text': '• 顶盖内侧增加拉链网袋', 'size': 17},
        ],
    },
    {
        'src': 'TimberRidgeDaypack_Spiral_Spec_Viewer_p1.jpg',
        'dst': 'TimberRidgeDaypack_Spiral_Spec_Viewer_p1_zh.jpg',
        'boxes': [
            {'box': (205, 3, 760, 42), 'text': 'Timber Ridge 日用背包 V2', 'size': 24, 'fill': 'sample', 'color': 'white'},
            {'box': (143, 18, 700, 90), 'text': '肩带内侧边缘需使用透气网布', 'size': 20},
            {'box': (380, 150, 795, 390), 'text': '#8 反装拉链的悬浮式抓绒里配件袋，位于包体背面上部。\n拉链两端均需设置止口。', 'size': 20, 'spacing': 4},
            {'box': (760, 115, 1410, 320), 'text': '双层 20MM 织带提手，底层加入橙色点缀织带。\n织带需在中部折叠后车缝固定。', 'size': 20, 'spacing': 4},
            {'box': (940, 245, 1490, 360), 'text': '#10 反装主拉链仅在此侧延伸进入腰翼', 'size': 20},
            {'box': (932, 350, 1260, 418), 'text': '拉链两侧加滚边', 'size': 20},
            {'box': (930, 415, 1520, 660), 'text': '20MM 侧压缩带配单调 Duraflex GF 插扣，\n并加入弹力织带尾端固定。', 'size': 20, 'spacing': 4},
            {'box': (960, 635, 1500, 790), 'text': '附件环，10MM 织带对折后中部车缝，\n并缝入接缝。', 'size': 20, 'spacing': 4},
            {'box': (55, 504, 400, 640), 'text': '#10 反装前幅配件拉链需隐藏', 'size': 20},
            {'box': (309, 992, 392, 1037), 'text': '接缝', 'size': 20},
            {'box': (494, 1085, 583, 1134), 'text': '滚边', 'size': 20},
            {'box': (797, 996, 1243, 1188), 'text': '20MM 织带配单调 Duraflex GF 插扣，沿织带通道\n延伸至单侧腰翼末端，并加入弹力织带固定环。', 'size': 20, 'spacing': 4},
        ],
    },
    {
        'src': 'TimberRidgeDaypack_Spiral_Spec_Viewer_p2.jpg',
        'dst': 'TimberRidgeDaypack_Spiral_Spec_Viewer_p2_zh.jpg',
        'boxes': [
            {'box': (205, 3, 760, 42), 'text': 'Timber Ridge 日用背包 V2', 'size': 24, 'fill': 'sample', 'color': 'white'},
            {'box': (1188, 245, 1508, 335), 'text': '丝印 LOGO', 'size': 20},
            {'box': (80, 340, 610, 460), 'text': '两处拉链均按示意加入止口', 'size': 20},
            {'box': (135, 640, 535, 840), 'text': '双层面料结构，撞色套结，\n织带夹缝车入。', 'size': 20, 'spacing': 4},
            {'box': (420, 1035, 1496, 1183), 'text': '包体此侧增加网布水瓶袋，需与侧片平贴车缝。袋口网布折返后在人字弹力包边上车缝，包边不可外露。', 'size': 20},
        ],
    },
    {
        'src': 'TimberRidgeDaypack_Spiral_Spec_Viewer_p3.jpg',
        'dst': 'TimberRidgeDaypack_Spiral_Spec_Viewer_p3_zh.jpg',
        'boxes': [
            {'box': (205, 3, 760, 42), 'text': 'Timber Ridge 日用背包 V2', 'size': 24, 'fill': 'sample', 'color': 'white'},
            {'box': (310, 145, 820, 260), 'text': '210D 笔电隔层，沿背墙顶部加弹力包边。', 'size': 20},
            {'box': (1040, 255, 1485, 415), 'text': '注意，拉链需一直延伸至侧腰翼，\n如下方绿色示意所示。', 'size': 20, 'spacing': 4},
        ],
    },
    {
        'src': 'TimberRidgeDaypack_Spiral_Spec_Viewer_p4.jpg',
        'dst': 'TimberRidgeDaypack_Spiral_Spec_Viewer_p4_zh.jpg',
        'boxes': [
            {'box': (205, 3, 760, 42), 'text': 'Timber Ridge 日用背包 V2', 'size': 24, 'fill': 'sample', 'color': 'white'},
            {'box': (252, 520, 491, 620), 'text': '15MM 胸带，\n中央双调节插扣', 'size': 20, 'spacing': 4},
            {'box': (1174, 367, 1396, 404), 'text': '透气网垫块', 'size': 20},
            {'box': (1276, 602, 1530, 688), 'text': '按示意在背板外缘包边', 'size': 20},
            {'box': (212, 964, 459, 1004), 'text': '单侧腰翼', 'size': 20},
            {'box': (1287, 978, 1526, 1018), 'text': '透气网腰靠', 'size': 20},
            {'box': (501, 1088, 905, 1190), 'text': '20MM 织带配双杠调节扣\n及双调 Duraflex GF 插扣', 'size': 20, 'spacing': 4},
        ],
    },
    {
        'src': 'TimberRidgeDaypack_Spiral_Spec_Viewer_p5.jpg',
        'dst': 'TimberRidgeDaypack_Spiral_Spec_Viewer_p5_zh.jpg',
        'boxes': [
            {'box': (205, 3, 760, 42), 'text': 'Timber Ridge 日用背包 V2', 'size': 24, 'fill': 'sample', 'color': 'white'},
            {'box': (900, 116, 1229, 158), 'text': '目标尺寸 / 容量 - 25L', 'size': 20},
            {'box': (900, 160, 1545, 292), 'text': '首轮样品先无需考虑配色与材料，\n优先把造型与结构确定下来。', 'size': 20, 'spacing': 4},
        ],
    },
]


def fit_font(draw, text, box, size):
    left, top, right, bottom = box
    width = right - left
    height = bottom - top
    current = size
    while current >= 12:
        font = ImageFont.truetype(FONT, current)
        bbox = draw.multiline_textbbox((0, 0), text, font=font, spacing=4)
        if bbox[2] - bbox[0] <= width and bbox[3] - bbox[1] <= height:
            return font
        current -= 1
    return ImageFont.truetype(FONT, 12)


def draw_boxed_text(image, config):
    box = config['box']
    left, top, right, bottom = box
    draw = ImageDraw.Draw(image)
    fill = config.get('fill', 'white')
    if fill == 'sample':
        sample_x = min(max(left + 3, 0), image.width - 1)
        sample_y = min(max(top + 3, 0), image.height - 1)
        fill = image.getpixel((sample_x, sample_y))
    draw.rectangle(box, fill=fill)
    text = config['text']
    spacing = config.get('spacing', 4)
    font = fit_font(draw, text, box, config.get('size', 20))
    bbox = draw.multiline_textbbox((0, 0), text, font=font, spacing=spacing)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    x = left + 2
    y = top + max(0, ((bottom - top) - text_h) / 2) - 1
    draw.multiline_text((x, y), text, font=font, fill=config.get('color', 'black'), spacing=spacing)


for page in PAGES:
    src = ASSETS / page['src']
    dst = ASSETS / page['dst']
    image = Image.open(src).convert('RGB')
    for config in page['boxes']:
        draw_boxed_text(image, config)
    image.save(dst, quality=92)
    print(f'Wrote {dst.name}')
