# Google Imagen 3 工业级实景生图规范与防翻车提示词库 (Imagen 3 Industrial Prompts)

在出海 B2B 视觉体系中，虚假或带有西方人面孔的素材会严重损害国内源头工厂的真实信任感。本项目确立了**100% 中国员工面孔约束**与**双轨中英官方品牌标识约束**的工程级生图标准。

---

## 一、 核心生图准则与负向约束 (Core Guidelines & Hard Constraints)

1. **绝对禁止出现外国/西方员工**：
   - 所有研发工程师、车间操作工、分析化学师、叉车师傅、业务经理必须为**清晰的中国专业人员（Chinese personnel / East Asian ethnicity）**；
   - 负向提示词必须写入：`caucasian, western face, blonde, blue eyes, generic stock photo model, fake smiling, AI plastic texture, anime, cartoon`。
2. **Logo 与公司标识双轨规范（上英文、下中文）**：
   - 画面中凡出现标牌、大屏、桶面、外墙或设备标识处，强制统一使用：
     $$\text{第一行（上面英文）：\textbf{FOSS LUBRICATION}}$$
     $$\text{第二行（下面中文）：\textbf{福斯润滑}}$$
   - 辅助文字可包含：`QUALITY CONTROL LABORATORY - QUANZHOU`、`BLENDING PLANT`、`BASE OIL TANK 10000T`。
3. **真实工业硬核感 (Industrial Truth)**：
   - 拒绝扁平无细节的 3D 渲染，强制要求工业纪实摄影质感（Photorealistic commercial documentary photography）；
   - 保留真实的管道法兰、PLC 触摸中控屏、不锈钢 15,000L 反应釜、金黄色抗磨液压油反光、UN 208L 钢桶金属漆质感。

---

## 二、 10 大核心场景提示词精准模板 (Prompt Templates)

### 1. 首页 Hero Slide 1：调配车间与中控工程师
```text
Photorealistic documentary commercial photography of a modern high-capacity lubricant blending plant in Quanzhou, China. An intelligent Chinese male chemical engineer in a white hardhat and professional blue work jacket is operating a glowing PLC digital touchscreen automation panel. In the background are massive stainless steel computerized blending tanks and reactors (15,000L) with stainless steel piping systems, valves, and sight glasses showing clear golden lubricating oil. In the background, prominent crisp industrial factory wall signage clearly displays the brand name in two lines: top line 'FOSS LUBRICATION', bottom line Chinese characters '福斯润滑'. Clean factory floor, authentic workshop depth of field, natural engineering lighting, Canon EOS R5 35mm lens, f/2.8, ISO 100, highly detailed, realistic industrial textures.
```

### 2. 首页 Hero Slide 2：ASTM 质检实验室与女化验师
```text
Photorealistic commercial photography of an advanced petroleum quality testing laboratory in Quanzhou, China. A professional Chinese female analytical chemist in a white lab coat, safety goggles, and hair neatly tied back is holding an Erlenmeyer glass flask containing clear golden amber hydraulic oil, inspecting its transparency and viscosity. On the modern laboratory bench are Tamson kinematic viscometer baths, digital Karl Fischer titrators, and analytical balances. On the background lab wall, a high-contrast illuminated sign displays in clean bold lettering: top line 'FOSS LUBRICATION', middle line Chinese '福斯润滑', bottom line 'QUALITY CONTROL LABORATORY - QUANZHOU'. High depth of field, sharp clinical focus, bright laboratory daylight illumination, authentic Chinese scientist, 8k resolution.
```

### 3. 首页 Hero Slide 3：208L 钢桶仓储与集装箱装柜
```text
Photorealistic industrial photography of an export container loading bay at a heavy industrial lubricant warehouse in China. A focused Chinese forklift driver in a high-visibility safety vest and yellow hardhat is driving an industrial forklift, carefully loading palletized 208L steel drums into a 20-foot shipping container. Rows of UN 1A1 heavy steel drums in navy blue and red baking enamel finish, cleanly stenciled with the white brand logo: top line 'FOSS LUBRICATION', bottom line Chinese '福斯润滑'. Background shows warehouse staging racks and ocean freight shipping containers. Wide angle 24mm industrial photography, realistic morning port sunlight, crisp industrial detail, Chinese workers.
```

### 4. About 工厂介绍：泉州调配厂全景与储罐群
```text
Commercial aerial and eye-level blended architectural photography of the modern blending plant of Quanzhou Foss Lubrication Technology Co., Ltd. Large industrial compound with modern blending buildings, automated warehouse, and towering vertical base oil storage silos (labeled 'BASE OIL TANK 10000T / FOSS'). The main plant building facade features a bold 3D stainless steel sign reading: top line 'FOSS LUBRICATION', bottom line Chinese characters '福斯润滑'. Chinese engineers in safety gear walking in the courtyard. Clear blue Fujian coastal sky, green landscaping, asphalt logistics driveway with tanker trucks, authentic industrial establishment, sharp detail, 16:9 aspect ratio.
```

### 5. Hydraulic Oil 液压油：高压系统与机电技术员
```text
Cinematic industrial photography focusing on precision hydraulic fluid testing and machine maintenance. A skilled Chinese hydraulic maintenance technician in safety helmet and protective gloves is inspecting precision digital pressure gauges, hydraulic manifolds, and clear fluid sight glasses showing golden L-HM 46 anti-wear hydraulic oil flowing under pressure. Beside the machinery is a blue 208L steel drum prominently printed with 'FOSS LUBRICATION / 福斯润滑'. Shallow depth of field, crisp focus on the engineer's concentrated face and high-pressure oil lines, industrial ambient lighting.
```

### 6. Industrial Oils 工业油：重型齿轮箱与机械工程师
```text
Industrial engineering photography of heavy industrial machinery lubrication inspection. An experienced Chinese mechanical engineer in protective gear and hardhat (with employee badge) is using an inspection light to examine the lubricated planetary gear teeth inside a heavy-duty industrial gearbox. Clean lubricating oil coating the gear surfaces. In the background workshop, neatly stacked drums and plant wall banners read 'FOSS LUBRICATION / 福斯润滑'. Authentic heavy manufacturing plant setting, dramatic side lighting, sharp mechanical details.
```

### 7. Packaging & Logistics 包装物流：厦门港集装箱监装
```text
Documentary commercial photography at Xiamen Port maritime container terminal, China. A Chinese female export logistics supervisor wearing a yellow hardhat and safety vest holds a clipboard and digital tablet, conducting final export inspection of palletized UN 208L steel drums inside an open ocean shipping container. Beside her, a Chinese forklift operator stages another pallet. On the steel container door and drum surfaces, bold clean stencil reads 'FOSS LUBRICATION / 福斯润滑'. Background features towering port container cranes, stacking yards, and coastal sky. Ultra-realistic, documentary photography.
```

### 8. Products 产品目录：自动化机器人灌装线
```text
Industrial high-tech photography of an automated robotic drum filling and packaging line for industrial lubricants. High-precision robotic arm positioning filling nozzles over 208L heavy steel drums and 1000L IBC totes. A Chinese female quality assurance inspector with protective glasses and digital tablet monitors the computerized weighing readout. Drums feature vibrant navy and crimson baked enamel coatings cleanly labeled 'FOSS LUBRICATION / 福斯润滑'. Modern clean manufacturing environment, polished epoxy floor, stainless steel reactors in the background, sharp bright lighting.
```

### 9. News 每日研报：国际能源情报与分析师团队
```text
Professional editorial photography of a global energy and petroleum market research room. A team of Chinese commodity analysts and economists wearing headsets are seated at modern multi-monitor trading desks, analyzing real-time Brent crude oil candles, Group II base oil price curves, and global tanker shipping route maps. On the central high-definition display wall, a glowing header displays: 'FOSS LUBRICATION / 福斯润滑 / GLOBAL PETROLEUM MARKET INTELLIGENCE'. Professional corporate atmosphere, soft daylight and LED screen glow, authentic Chinese financial and industry researchers.
```

### 10. Contact 联系我们：出口技术咨询与销售中心
```text
Corporate commercial photography inside the customer technical service and export sales center of Quanzhou Foss Lubrication Technology Co., Ltd. Chinese export sales engineers and technical lubrication consultants working collaboratively at workstations with dual screens, reviewing international client inquiries and laboratory CoA test certificates. Behind a clear glass partition, the internal testing laboratory and chemical testing apparatus are visible. On the office accent wall, brushed aluminum 3D letters read: top line 'FOSS LUBRICATION', bottom line Chinese '福斯润滑'. Bright modern corporate office, confident and welcoming Chinese team.
```
