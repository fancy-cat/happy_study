import { Button, Form, Input, Radio,Checkbox } from 'antd';
import React, { useState } from 'react';
const { TextArea } = Input;
export default function Home() {
  const [form] = Form.useForm();
  const [type] = useState(0);
  const typeOptions = [
    {
      label: '单词',
      value: 0
    },
    {
      label: '句子',
      value: 1
    },
    {
      label: '笔记',
      value: 2
    },
    {
      label: '疑问',
      value: 3
    },
  ];
  const toneOptions = [0,1,2,3,4,5,6,7,8,9];
  const onChange = (checkedValues) => {
    console.log('checked = ', checkedValues);
  };
  return <div>
     <Form
      form={form}
      style={{
        maxWidth: 600,
      }}
      colon={false}
    >
      <Form.Item name="layout">
        <Radio.Group
          optionType="button"
          value={type}
          options={typeOptions}
        />
      </Form.Item>
      <Form.Item label="单词" name="layout">
        <Input placeholder="请输入" />
      </Form.Item>
      <Form.Item label="假名">
        <Input placeholder="请输入" />
      </Form.Item>
      <Form.Item label="声调">
        <Checkbox.Group
          options={toneOptions}
          defaultValue={[]}
          onChange={onChange}
        />
      </Form.Item>
      <Form.Item label="句子">
      <TextArea rows={2} placeholder="请输入"/>
      </Form.Item>
      <Form.Item label="备注">
        <TextArea rows={4} placeholder="请输入"/>
      </Form.Item>
      <Form.Item>
        <Button type="primary">提交</Button>
      </Form.Item>
    </Form>
  </div>
}